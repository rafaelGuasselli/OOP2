def validaNome(nome):
    return len(nome) > 3

def validaIdade(idade):
    return idade >= 0 and idade <= 150

def validaSalario(salario):
    return salario > 0

def validaSexo(sexo):
    return sexo in ["m", "f"]

def validaEstadoCivil(estadoCivil):
    return estadoCivil in ['s', 'c', 'v', 'd']


while True:
    try:
        nome = validaNome(input())
        idade = validaIdade(int(input()))
        salario = validaSalario(int(input()))
        sexo = validaSexo(input())
        estadoCivil = validaEstadoCivil(input())

        if (not nome):
            raise Exception("Nome invalido")

        if (not idade):
            raise Exception("Idade invalido")

        if (not salario):
            raise Exception("Salario invalido")
        
        if (not sexo):
            raise Exception("Sexo invalido")

        if (not estadoCivil):
            raise Exception("Estado Civil invalido")
    
        print("Sucesso!")
        break
    except Exception as exception:
        print(exception)
        pass
