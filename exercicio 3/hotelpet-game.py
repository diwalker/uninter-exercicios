def ent():
	print("### HOTEL PETLOVERS ### cada numero representa um quarto")
	print("[1 2 3 4]")
	print("[5 6 7 8]\n")
	print("Quartos com * == ocupados && Quartos com _ == disponiveis")
	print("GATO(G) - CÃO(C) - RATO(R) - OSSO(O) - QUEIJO(Q)\n")


def vit() -> object:  # função de mensagem
	print("Você venceu! XD")


def der():  # função de mensagem
	print("Você perdeu! :(")


def f1(valida: object = None) -> object:  # função de fases
	valida = ["*", "*", "G", "G", "R", "R", "*", "*"]
	fase = ["*", "*", "_", "G", "R", "_", "*", "*"]
	hospedes = ("Rato", "Gato")
	print('FASE 01:')
	print('Escola um quarto para: \n-Rato(R)\n-Gato(G)')
	print('Disponíveis: 3 e 6')
	print(fase[:4])
	print(fase[4:])
	for h in hospedes:
		quarto = int(input("Qual quarto para o " + h + "?"))
		fase[quarto - 1] = h[0]

	return False if valida == fase else True


def f2() -> object:  # função de fases
	valida = ["O", "*", "*", "*", "*", "C", "C", "C"]
	fase = ["_", "*", "*", "*", "*", "C", "_", "_"]
	hospedes = ("Cão", "Cão", "Osso")
	print('\nFASE 02!')
	print('Escolha um quarto quarto para: \n-Cão(C)\n-Cão(C)\n-Osso(O)')
	print('Disponíveis: 1, 7 e 8')
	print(fase[:4])
	print(fase[4:])
	for h in hospedes:
		quarto = int(input("Qual quarto para o " + h + "? "))
		fase[quarto - 1] = h[0]

	return False if valida == fase else True


def f3() -> object:  # função de fases
	valida = ["R", "*", "*", "*", "O", "G", "G", "*"]
	fase = ["_", "*", "*", "*", "_", "G", "_", "*"]
	hospedes = ("Gato", "Rato", "Osso")
	print('\nFASE 03!')
	print('Escolha um quarto quarto para: \n-Gato(G)\n-Rato(R)\n-Osso(O)')
	print('Disponíveis: 1, 5 e 7')
	print(fase[:4])
	print(fase[4:])
	for h in hospedes:
		quarto = int(input("Qual quarto para o " + h + "? "))
		fase[quarto - 1] = h[0]

	return False if valida == fase else True


def f4() -> object:  #função de fases
	valida = ["Q", "O", "Q", "*", "*", "R", "*", "*"]
	fase = ["_", "_", "_", "*", "*", "R", "*", "*"]
	hospedes = ("Queijo", "Queijo", "Osso")
	print('\nFASE 04!')
	print('Escolha um quarto quarto para: \n-Queijo(Q)\n-Queijo(Q)\n-Osso(O)')
	print('Disponíveis: 1, 2 e 3')
	print(fase[:4])
	print(fase[4:])
	for h in hospedes:
		quarto = int(input("Qual quarto para o " + h + "? "))
		fase[quarto - 1] = h[0]

	return False if valida == fase else True


ent()  # chama a função até que um retorno
while True:
	fase = f1()
	if fase:
		der()
		break
	fase = f2()
	if fase:
		der()
		break
	fase = f3()
	if fase:
		der()
		break
	fase = f4()
	if fase:
		der()
		break
	else:
		vit()
		break
