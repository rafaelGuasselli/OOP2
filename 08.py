from functools import reduce
numeros = list(map(int, input().split()))
media = reduce(lambda a,b:a+b, numeros)/len(numeros)
print(media)