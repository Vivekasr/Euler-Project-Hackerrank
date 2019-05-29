#!/bin/python3

import sys


def strmult(strnum):
    mult = 1
    for char in strnum:
        mult = mult*int(char)

    return mult


def getMaxProduct(n, k):
    lst = []
    strnum = str(n)
    for i in range(0, len(strnum)-k+1):
        element = strnum[i:i+k]
        lst.append(strmult(element))

    lst.sort()
    print(lst[len(lst)-1])


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    getMaxProduct(num, k)
