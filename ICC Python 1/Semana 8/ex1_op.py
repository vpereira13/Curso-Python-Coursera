"""
Exercício 1 - Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
"""

def maior_elemento(lista):
	"""Função que retorna o maior elemento de uma lista

	Args:
		lista (list): lista de números inteiros

	Returns:
		int: maior elemento da lista
	"""
	lista.sort()

	return lista[len(lista)-1]