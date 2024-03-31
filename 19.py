from functools import reduce

def parseParamsElements(params):
	elementos = []
	for elemento in params:
		if isinstance(elemento, list):
			elementos.extend(elemento)
		else:
			elementos.append(elemento)
	return elementos

def max(*lista):
	elementos = parseParamsElements(lista)
	maior = elementos[0]
	for numero in elementos:
		if numero > maior:
			maior = numero
	return maior

def min(*lista):
	elementos =	parseParamsElements(lista)
	menor = elementos[0]
	for numero in elementos:
		if numero < menor:
			menor = numero
	return menor
while True:
    numeros = list(map(int, input().split()))
    if (reduce(lambda a,b: a and (b >= 0 and b <= 1000), numeros, True)): 
        print("Numero invalidos")
        break

print(max(numeros))
print(min(numeros))
print(reduce(lambda a,b:a+b, numeros))
