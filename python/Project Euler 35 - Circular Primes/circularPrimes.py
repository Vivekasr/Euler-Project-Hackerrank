from math import sqrt


def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for x in range(4, n+1, 2):
        primes[x] = False

    for x in range(3, int(sqrt(n))+1, 2):
        if(primes[x]):
            for y in range(x*x, n+1, x):
                primes[y] = False

    return primes


def rotate(n):
    n = str(n)
    return n[1:]+n[:1]


def isRotatable(n, primes):
    for x in range(2, n):
        n = rotate(n)
        if not primes[int(n)]:
            return False
    return True


def main(n):
    primes = sieve(n)
    result = 0
    for x in range(2, len(primes)):
        if(isRotatable(x, primes)):
            result += x

    print(result)


a = int(input())
main(a)
