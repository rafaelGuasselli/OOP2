populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015

anos = 0
while populacaoA < populacaoB:
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    anos += 1

print(anos)