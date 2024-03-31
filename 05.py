populacaoA = int(input("populacao inicial a: "))
crescimentoA = float(input("crescimento de a: ")) / 100 + 1
populacaoB = int(input("populacao inicial a: "))
crescimentoB = float(input("crescimento de b:  ")) / 100 + 1

anos = 0
while populacaoA < populacaoB:
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    anos += 1

print(anos)