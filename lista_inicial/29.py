precos = []
while(True):
	preco = float(input())
	if preco == 0:
		break
	precos.append(preco)

print("Lojas Quase Dois - Tabela de preços")
for i in range(len(precos)):
    print("{:n} - R$ {:.2f}".format(i+1, precos[i]))