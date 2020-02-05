#!/usr/bin/env python

from argparse import ArgumentParser
from os import path, listdir, stat
from os.path import isfile, join
from time import sleep
import subprocess
import threading


class Shell():

    def __init__(self, objFolder, name, link):
        self.__objFolder = objFolder
        self.__name = name
        self.__link = link

    def run(self):
        while True:
            i = input("> ")
            if i == "exit":
                break
            if i == "comp":
                try:
                    subprocess.run(self.__genCommand())
                except Exception:
                    pass

    def __genCommand(self) -> [str]:
        files = [self.__objFolder + "/" + f for f in listdir(self.__objFolder) if isfile(join(self.__objFolder, f)) and f.endswith(".cpp.o")]
        s = "g++ -o " + self.__name + " " + " ".join(files) + " -l"
        s += " -l".join(self.__link)
        print(s)
        return s.split(" ")


class ConfReader():

    def __init__(self, file):
        self.__file = file
        self.__name = None
        self.__link = None
        self.__include = None
        self.__options = None

        self.__parse()

    def __parse(self):
        with open(self.__file) as fd:
            lines = fd.readlines()

        for l in lines:
            t = l.strip().split(":")
            if t[0] == "name":
                self.__name = t[1]
            elif t[0] == "link":
                self.__link = t[1].split(",")
            elif t[0] == "include":
                self.__include = t[1].split(",")
            elif t[0] == "options":
                self.__options = t[1].split(",")

        # print(self.__link)
        # print(self.__include)
        # print(self.__options)

    def __bool__(self) -> bool:
        return self.__link != None and self.__include != None and self.__options != None and self.__name != None

    def getInfos(self) -> (str, str, str, str):
        return self.__name, self.__link, self.__include, self.__options


class Compile():

    def __init__(self, srcFolder, objFolder, link, include, options):
        self.__srcFolder = srcFolder
        self.__objFolder = objFolder
        self.__link = link
        self.__include = include
        self.__options = options
        self.__sources = self.__getSources()
        #print(self.__sources)

    def __getSources(self):
        files = [f for f in listdir(self.__srcFolder) if isfile(join(self.__srcFolder, f)) and f.endswith(".cpp")]
        dates = [int(stat(join(self.__srcFolder, f)).st_mtime) for f in files]
        return dict(zip(files, dates))

    def reload(self, e: threading.Event):
        while not e.isSet():
            for old, new in zip(self.__sources.items(), self.__getSources().items()):
                name, oldStamp = old
                _, newStamp = new
                if newStamp > oldStamp:
                    subprocess.run(self.__createCommand(name))
                    self.__sources[name] = newStamp
            sleep(1)

    def __createCommand(self, name):
        s = f"g++ -c {join(self.__srcFolder, name)}"
        s += " -o " + join(self.__objFolder, name + ".o ")
        s += " ".join(self.__options) + " -I"
        s += " -I".join(self.__include) + " -l"
        s += " -l".join(self.__link)
        #print(s.split(" "))
        return s.split(" ")


def main():
    parse = ArgumentParser("Hot reloading for C++ files")
    parse.add_argument("src", help="folder where sources are")
    parse.add_argument("obj", help="folder where objects fille will be")
    parse.add_argument("config", help="configuration file")
    args = parse.parse_args()

    srcFolder = path.abspath(args.src)
    objFolder = path.abspath(args.obj)

    c = ConfReader(args.config)
    if c:
        name, link, include, options = c.getInfos()
        comp = Compile(srcFolder, objFolder, link, include, options)

        e = threading.Event()
        t = threading.Thread(target=comp.reload, args=(e,))
        t.start()

        s = Shell(objFolder, name, link)
        s.run()

        e.set()
        t.join()
    else:
        print("Encule")
        exit(84)


if __name__ == "__main__":
    main()