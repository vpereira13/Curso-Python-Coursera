"""
Exercício 1: Letras maiúsculas

Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que contém os valores de cada caractere. Ver http://equipe.nce.ufrj.br/adriano/c/apostila/tabascii.htm

Note que para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres que não estejam presentes na tabela ASCII apresentada, como ç, á, É, ã, etc.

Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função ord apresentada nas aulas.

Exemplos:

maiusculas('Programamos em python 2?')
# deve devolver 'P'

maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'
"""

def maiusculas(frase):
	"""Função que dada uma string, devolve uma outra string contendo somente
	as letras maiúsculas da string dada como parametro, na ordem que aparece

	Args:
		frase (str): string a ser analisada

	Returns:
		str: uma string contendo somente as letras maiúsculas da string original
	"""
	string = ""
	for i in range(len(frase)):
		if ord(frase[i]) > 64 and ord(frase[i]) < 91:
			string += frase[i]

	return string
