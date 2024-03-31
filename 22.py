num = int(input())

div = 2
divosr = [1]

while num > div:
    if num % div == 0:
        divosr.append(div)
    div += 1

if len(divosr) == 1:
    print("primo")
else:
    print("composto")
divosr.append(num)
print(*divosr)
