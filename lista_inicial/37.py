pesos = {}
alturas = {}

while True:
	codigo = int(input()) 
	if codigo == 0:
		break

	altura, peso = map(int, input().split())
	pesos[codigo] = peso
	alturas[codigo] = peso

