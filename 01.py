while True:
	try:
		nota = int(input())
		if nota < 0 or nota > 10:
			raise Exception("Nota invalida!")
	except:
		print("Nota invalida!")