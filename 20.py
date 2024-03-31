while True:
    n = int(input())

    if n < 0 or n > 16:
        break

    numero = 1
    for i in range(1, n+1):
        numero *= i
    print(numero)