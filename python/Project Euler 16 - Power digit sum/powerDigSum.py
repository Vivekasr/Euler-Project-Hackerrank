t = int(input())
for a0 in range(t):
    n = int(input())
    a = 2**n
    s = 0
    while a:
        s += a % 10
        a //= 10
    print(s)
