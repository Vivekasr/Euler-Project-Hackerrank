#!/bin/python3

import sys


def fib(n):
    lst = []
    a, b = 1, 1
    for i in range(100):
        a, b = b, a+b
        lst.append(a)
    count = 0
    for num in lst:
        if num < n:
            if num % 2 == 0:
                count += num
    print(count)
