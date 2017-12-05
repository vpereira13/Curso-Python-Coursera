"""
Exercício 1: Ordenação com insertion sort

Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo insertion sort.
"""

def insertion_sort(lista):
	"""Função para ordenar lista seguindo o algoritmo insertion sort

	Args:
		lista (list): lista de elementos a ser ordenada

	Returns:
		list: lista ordenada
	"""
	for i in range(1, len(lista)):
		temp = lista[i]
		indice = i

		while indice > 0 and lista[indice-1] > temp:
			lista[indice] = lista[indice-1]
			indice = indice - 1

		lista[indice] = temp

	return lista