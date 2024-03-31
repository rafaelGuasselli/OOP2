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

numeros = list(map(int, input().split()))
print(max(numeros))