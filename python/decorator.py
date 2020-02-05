#!/usr/bin/env python

user = "Casu"


def decorate(func):
    print(
        "Yé soui dan la fonction 'decorate', pwochaine fonction: {}".format(
            func.__name__
        )
    )

    def nope(*args):
        print("Not good enough to yeet properly")

    if user == "Pro Yeeter":
        return func
    return nope


#@decorate
def yeet(*args):
    print("Yeeting ", end="")
    print(", ".join(args))


#yeet("a", "b", "c", "d")


class Plouf:
    def notAStaticMethod(self):
        self.splash()
        print("I'm not static mate")

    @classmethod
    def pilou(cls):
        cls.notAStaticMethod(cls)
        print("Incroyable du cul")
        return cls

    @staticmethod
    def splash():
        print("Gonna splash !")


#Plouf().splash()
#Plouf.splash()

#Plouf().notAStaticMethod()
#Plouf.notAStaticMethod()

#Plouf.pilou().splash()


class Pluf(Plouf):

    def notAStaticMethod(self):
        print("I'm not static bwo !!")

    @staticmethod
    def splash():
        print("I'm sploushing !!!")

Pluf().splash()
Pluf.splash()

Pluf().notAStaticMethod()
Pluf.notAStaticMethod(Pluf())





