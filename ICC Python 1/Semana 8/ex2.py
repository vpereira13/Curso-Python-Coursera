"""
Exercício 2 - Soma dos elementos de uma lista

Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
"""

def soma_elementos(lista):
	"""Função que calcula o somatório de todos os elementos da lista

	Args:
		lista (list): lista de números inteiros

	Returns:
		int: soma de todos os elementos da lista
	"""
	soma = 0

	for elemento in lista:
		soma += elemento

	return soma