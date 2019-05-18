def factsum(n):
    mult = 1
    for i in range(1, n+1):
        mult = mult*i
    a = str(mult)
    add = 0
    for ints in a:
        add = add+int(ints)
    print(add)


num = int(input())
for i0 in range(num):
    n = int(input())
    factsum(n)
