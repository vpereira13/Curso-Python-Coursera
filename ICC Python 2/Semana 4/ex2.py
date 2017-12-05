"""
Exercício 2: Busca sequencial

Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Exemplo:

busca(['a', 'e', 'i'], 'e')
# deve devolver => 1

busca([12, 13, 14], 15)
# deve devolver => False
"""

#import pytest

def busca(lista, elemento):
	"""Função para fazer uma busca de um número de forma
	sequencial em uma lista

	Args:
		lista (list): lista de alguma coisa, pode ser int, float, char
		elemento (int/float/char): elemento a ser buscado na lista

	Returns:
		int/bool: Se achar o elemento na lista, retorna o índice onde
		ele se encontra. Caso não achar, retorna False
	"""
	for i in range(len(lista)):
		if lista[i] == elemento:
			return i

	return False

"""
# Casos de teste

@pytest.mark.parametrize("lista, elemento, esperado",[
	(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 'g', 6),
	([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15, False),
	([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 2),
	([1, 'a', 3, 'c', 5, 'd', 7, 8, 9, ], 'c', 3),
	([1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 10], 4, 3),
	([1, 'a', 3, 'c', 5, 'd', 7, 8, 9, ], 'ca', False)
	])
def testBusca(lista, elemento, esperado):
	assert busca(lista, elemento) == esperado
"""