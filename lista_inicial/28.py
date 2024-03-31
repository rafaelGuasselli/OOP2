qtdCds = int(input())

media = 0
total = 0

for i in range(qtdCds):
    cd = int(input())
    total += cd

media = total/qtdCds
print("Total: {:n}, Media: {:.2f}".format(total, media)) 