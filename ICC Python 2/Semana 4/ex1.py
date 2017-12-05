"""
Exercício 1: Lista ordenada

Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.
"""

#import pytest

def ordenada(lista):
	"""Função para verificar se uma certa lista está ordenada de forma crescente

	Args:
		lista (list): lista de números inteiros

	Returns:
		bool: True, se tiver ordenada e False, se não estiver ordenada
	"""
	for i in range(len(lista)-1):
		if lista[i] > lista[i+1]:
			return False

	return True

"""
# Casos de teste

@pytest.mark.parametrize("lista, esperado",[
	([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
	([0, 1, 2, 3, 4, 5, 10, 2, 3, 4, 5], False),
	([-15, 0, 1, 2, 3, 4, 5, 6, 7, 7, 7], True),
	([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True),
	([-14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4], True),
	([0, 2, 3, 4, 5, 6, 1231, 12311, 1231231, 123123, -1], False)
	])
def testaOrdenacao(lista, esperado):
	assert ordenada(lista) == esperado
"""