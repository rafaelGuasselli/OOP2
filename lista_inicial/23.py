from math import floor

def testaPrimo(n):
    div = 2
    primo = True
    cont = 1
    
    if n == 1:
        return False, 0

    while n >= div*div:
        if n % div == 0:
            return False, floor(n**(0.5))
        div += 1

    return True, floor(n**(0.5))



num = int(input())
cont = 0
for i in range(1, num + 1):
    primo, div = testaPrimo(i)
    cont += div
    if primo:
        print("{:n}, num divisoes: {:n}".format(i, div))

    
print(cont)