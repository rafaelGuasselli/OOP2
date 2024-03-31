base = int(input())
exp = int(input())
cont = 1

if exp < 0:
    exp = -exp
    base = 1/base

while exp > 0:
    cont *= base
    exp -= 1

print(cont)