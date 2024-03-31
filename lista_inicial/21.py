num = int(input())

div = 2
primo = True

while num > div*div:
    if num % div == 0:
        primo = False
    div += 1

if primo:
    print("primo")
else:
    print("composto")
