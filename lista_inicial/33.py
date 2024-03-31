media = 0
menor = 1000000000000000
maior = -100000000000000
count = 0
while(True):
	temperatura = float(input())
	if temperatura == 0:
		break

	if temperatura < menor: menor = temperatura
	if temperatura > maior: maior = temperatura
	media += temperatura
	count += 1

print("Media {:.2f}, Menor: {:.2f}, Maior: {:.2f}".format(media/max(count, 1), menor, maior))
