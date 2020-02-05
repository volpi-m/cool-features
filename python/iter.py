#!/usr/bin/env python

import itertools

for i in itertools.accumulate([x*x for x in range(1, 20)]):
    print(i)
