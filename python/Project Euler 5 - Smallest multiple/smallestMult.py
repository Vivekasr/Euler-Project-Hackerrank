#!/bin/python3

import sys
from math import gcd


def findlcm(lst):
    lcm = lst[0]
    for i in lst[1:]:
        lcm = lcm*int(i/gcd(lcm, i))
    print(lcm)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lst = []
    for i in range(1, n+1):
        lst.append(i)

    findlcm(lst)
