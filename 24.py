from functools import reduce

notas = list(map(int, input().split()))
media = reduce(lambda a,b: a + b, notas) / len(notas)

print(media)
