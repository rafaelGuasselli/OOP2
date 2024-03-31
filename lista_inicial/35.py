from math import floor

def testaPrimo(n):
	div = 2
	primo = True
	
	if n == 1:
		return False

	while n >= div*div:
		if n % div == 0:
			return False
		div += 1
	return True

num = int(input())
for i in range(1, num + 1):
	primo = testaPrimo(i)
	if primo:
		print("{:n}".format(i))