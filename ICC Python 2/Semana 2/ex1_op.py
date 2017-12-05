"""
Exercício 1: Contando vogais ou consoantes

Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.

Exemplos:

conta_letras('programamos em python')
# deve devolver 6

conta_letras('programamos em python', 'vogais')
# deve devolver 6

conta_letras('programamos em python', 'consoantes')
# deve devolver 13
"""

def conta_letras(frase, contar="vogais"):
	"""Função que conta uma certa quantidade de letras, vogais
	ou consoantes, de uma frase dependendo do segundo parâmetro

	Args:
		frase (str): uma frase sem acentuações
		contar (str, optional): qual tipo de letra é para ser contado
		vogais (padrão) ou consoantes

	Returns:
		int: número de vogais ou de consoantes contidas na frase
	"""
	contador = 0

	if contar is "vogais":
		for i in frase:
			if i in "aeiouAEIOU":		#verifica se são as vogais
				contador += 1
	else:
		for i in frase:
			if not i in "aeiouAEIOU ":	#verifica se não as vogais nem espaço
				contador += 1

	return contador
