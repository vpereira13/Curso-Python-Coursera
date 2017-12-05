"""
Exercício 1: Busca binária

Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.

Exemplo:

busca(['a', 'e', 'i'], 'e')
1
# deve devolver => 1

busca([1, 2, 3, 4, 5], 6)
2
3
4
# deve devolver => False

busca([1, 2, 3, 4, 5, 6], 4)
2
4
3
# deve devolver => 3
"""

def busca(lista, elemento):
	"""Função busca binária com o seguinte diferencial,
	a cada iteração imprime o valor do meio

	Args:
		lista (list): lista de elementos onde será procurado
		elemento (int/char/float): elemento a ser procurado

	Returns:
		int/bool: inteiro, valor do índice se caso achar o elemento
		na lista. False, se não achar o elemento na lista
	"""
	primeiro = 0
	ultimo = len(lista) - 1

	while primeiro <= ultimo:
		meio = (primeiro + ultimo)//2
		print(meio)
		if lista[meio] == elemento:
			return meio
		else:
			if elemento > lista[meio]:
				primeiro = meio + 1
			else:
				ultimo = meio - 1

	return False
