fatorial = int(input())
saida = "{:n}! = ".format(fatorial)
resultado = 1

for i in range(fatorial, 0, -1):
	saida += str(i)
	resultado *= i
	if i != 1:
		saida+=" . "
print(saida+" = {:n}".format(resultado))
		