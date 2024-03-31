from functools import reduce

num = list(map(int, input().split()))
impar = reduce(lambda a,b: (a + (b % 2)), num, 0)
par = len(num) - impar

print("impares: {:n}\npar: {:n}".format(impar, par))

