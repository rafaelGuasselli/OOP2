numero = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if fim < comeco:
    print("Tabuada vazia, pois fim menor que o começo!")
else:
	print("Vou montar a tabuada de {:n} começando em {:n} e terminando em {:n}:".format(numero, comeco, fim))
 
for i in range(comeco, fim+1):
    print("{:n} X {:n} = {:n}".format(numero, i, i * numero))