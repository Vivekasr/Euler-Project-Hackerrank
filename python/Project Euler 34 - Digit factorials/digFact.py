import math


def curiousnum(n):
    resultsum = 0
    for i in range(n):
        if (i > 10):
            csum = 0
            b = i
            while(i > 0):
                a = i % 10
                csum += math.factorial(a)
                i = i//10

            if(csum % b == 0):
                resultsum += b

    print(resultsum)


a = int(input())
curiousnum(a)
