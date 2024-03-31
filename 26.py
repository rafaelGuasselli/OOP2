TOTAL_CANDIDATOS = 3
qtdEleitores = int(input())
votos = [0] * TOTAL_CANDIDATOS

for i in range(qtdEleitores):
	voto = -1
	while voto < 0 or voto >= TOTAL_CANDIDATOS:
		voto = int(input("Voto do eleitor {:n}: ".format(i+1))) - 1
	votos[voto] += 1

for i in range(TOTAL_CANDIDATOS):
	print("Total de votos do candidato {:n}: {:n}".format(i+1, votos[i]))