#!/bin/python3

import sys


def is_palindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev*10+dig
        n = n//10
    return(temp == rev)


def factors_of_number(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return(factors)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = ((n-1)//11)*11  # All six digit palindromes divisible by 11.
    three_digit_factors = "FALSE"
    while x > 0:
        if is_palindrome(x):
            factors = factors_of_number(x)
            factors_100 = [i for i in factors if i >= 100 and i < 1000]
            for j in range(0, len(factors_100)):
                if x//factors_100[j] >= 100 and x//factors_100[j] < 1000:
                    three_digit_factors = "TRUE"
        if three_digit_factors == "TRUE":
            break
        x -= 11
    print(x)
