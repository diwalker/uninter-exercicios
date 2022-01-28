import typing

while True:
	aluno: dict[str, typing.Union[str, int]] = {}
	aluno['nome'] = str(input('Digite o nome do aluno: ')) #ENTRADA DO NOME DO ALUNO
	aluno['idade'] = int(input(f'Digite a idade de {aluno["nome"]}: '))  #ENTRADA DA IDADE DO ALUNO

	if aluno['idade'] <= 5: #CASO ALUNO TENHA MENOS DE 5 ANOS
		aluno['ensino'] = 'Ensino Infantil'

	elif aluno['idade'] >= 6 and aluno['idade'] <= 10: #CASO ALUNO TENHA ENTRE 6 E 10 ANOS
		aluno['ensino'] = 'Ensino Fundamental I'

	elif aluno['idade'] > 10 and aluno['idade'] <= 14: #CASO ALUNO TENHA ENTRE 11 E 14 ANOS
		aluno['ensino'] = 'Ensino Fundamental II'

	elif aluno['idade'] >= 15: #CASO ALUNO TENHA ACIMA DE 15 ANOS
		aluno['ensino'] = 'Ensino Médio'

	for k, v in aluno.items(): #ITERAÇÃO
		print(f'{k}: {v}')

	print('Você quer continuar?\n[ 0 ] Não\n[  1] Sim')
	opc = int(input('R: '))

	if opc == 0: #OPC == RESPOSTA, CASO A ENTRADA SEJA == 0, O SCRIPT FECHA
		break
