from functools import reduce
qtdTurmas = int(input())
turmas = []

for i in range(qtdTurmas):
	qtdAlunos = int(input())
	if (qtdAlunos > 40):
		raise Exception("Turma grande de mais!")
	turmas.append(qtdAlunos)

print(reduce(lambda a,b:a+b, turmas)/qtdTurmas)