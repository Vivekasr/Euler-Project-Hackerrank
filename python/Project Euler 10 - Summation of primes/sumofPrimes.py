#!/bin/python3

import sys


def SieveOfEratosthenes(n):
    ans = 0
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            ans += p

    print(ans)


t = int(input().strip())
lst = []
for a0 in range(t):
    n = int(input().strip())
    lst.append(n)

for i in lst:
    SieveOfEratosthenes(i)
