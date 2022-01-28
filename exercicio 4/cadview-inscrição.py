import random
from operator import itemgetter


def ins() -> object: #dicionario das entradas do usuario
	{}
	voucher: int = random.randint(100, 400)
	nome = input("Digite o seu nome: ")
	email = input("Digite o seu email: ")
	fone = input("Digite o seu telefone: ")
	curso = input("Digite o seu curso: ")

	dic_temp = {'Voucher': voucher,
	            'Nome': nome,
	            'Email': email,
	            'Telefone': fone,
	            'Curso': curso
	            }
	return dic_temp


def view(bd):  # visualiza os dados na lista de dicionarios.
	print("\n")
	print("*" * 7 + " LISTA DE INSCRITOS " + "*" * 7)
	v = list(map(itemgetter('Voucher'), bd))
	n = list(map(itemgetter('Nome'), bd))
	e = list(map(itemgetter('Email'), bd))
	t = list(map(itemgetter('Telefone'), bd))
	c = list(map(itemgetter('Curso'), bd))

	for i in range(len(bd)):
		print(f"Voucher   : {v[i]}")
		print(f"Nome      : {n[i]}")
		print(f"Email     : {e[i]}")
		print(f"Telefone  : {t[i]}")
		print(f"Curso     : {c[i]}")
	print("\n")


# declaração de variavris
bd = list()
stop = 3

# main
while stop != 1:
	print("\n")
	print("*" * 7 + " MENU " + "*" * 7)
	print("1 - Nova inscrição")
	print("2 - Visualizar inscrição")
	print("3 - Encerrar")
	opcsel: int = int(input("Opção escolhida: "))

	if opcsel == 3:
		stop = 1
	elif opcsel == 1:
		bd.append(ins())
	elif opcsel == 2:
		view(bd)
	else:
		print("\nErro: Digite1 uma opção válida!\n")
