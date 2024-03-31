from functools import reduce
qtdPessoas = int(input())
idades = []
for i in range(qtdPessoas):
    idades.append(int(input()))

media = reduce(lambda a,b:a+b, idades) / len(idades)


if media <= 25:
    print("jovem")
elif media <= 60:
    print("adulta")
else:
    print("idosa")
