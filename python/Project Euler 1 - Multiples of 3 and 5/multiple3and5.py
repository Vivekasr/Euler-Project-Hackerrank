#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    b = n-1
    a = (3*((b//3)*((b//3)+1)))//2+((5*(b//5)*((b//5)+1)))//2 - \
        ((15*(b//15)*((b//15)+1)))//2
    print(int(a))
