from functools import reduce
produtos = []
while(True):
	produto = float(input())
	if produto == 0:
		break
	produtos.append(produto)

print("Lojas tabajara")
for i in range(len(produtos)):
    print("Produto {:n}: R$ {:.2f}".format(i+1, produtos[i]))

dinheiro = int(input())
troco = dinheiro - reduce(lambda a, b: a+b, produtos)
print("Dinheiro: R$ {:.2f}".format(dinheiro))
print("Troco: R$ {:.2f}".format(troco))
