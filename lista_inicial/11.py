from functools import reduce
esq = int(input())
dirr = int(input())

for i in range(esq, dirr+1):
    print(i)
soma = reduce(lambda a,b:a+b, list(range(esq,dirr+1)))
print(soma)