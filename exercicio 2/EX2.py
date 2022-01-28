def letconv(letter):  #AQUI A FUNÇÃO QUE CONVERTE LETRAS EM SIMBOLOS
	letter = letter.upper()

	if letter != 'A':
		if (letter == 'E'):
			return '&'

		if letter != 'I':
			if (letter == 'O'):
				return '#'

			if letter != 'U':
				return
			return '*'

		return '!'

	return '@'


def main():
	nome: str = input("DIGITE SEU NOME: ")

	new_name = ''

	for i in nome:  #ITERA DAS LETRAS DA PALAVRA

		if (
			i.upper() == 'A' or
			i.upper() == 'E' or
			i.upper() == 'I' or
			i.upper() == 'O' or
			i.upper() == 'U'):  #VERIFICA SE TEM VOGAL OU NÃO
			new_name += letconv(i.upper())  #CONVERTE AQUI

		else:

			new_name += i.upper()

	print(new_name)


if __name__ == '__main__':
	main()
