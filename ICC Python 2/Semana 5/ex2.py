"""
Exercício 2: Ordenação com bubble sort

Implemente a função bubble_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo bubble sort.

Além de devolver uma lista ordenada, ao longo do processamento sua função deve imprimir o estado atual da lista toda vez que fizer uma alteração em seus elementos.

Exemplo:

bubble_sort([5, 1, 4, 2])
[1, 5, 4, 2]
[1, 4, 5, 2]
[1, 4, 2, 5]
[1, 2, 4, 5]
# deve devolver [1, 2, 4, 5]
"""

def bubble_sort(lista):
	"""Função bubble sort com uma modificação, cada troca de valores é
	impressa a lista a ser ordenada

	Args:
		lista (list): lista de inteiros a ser ordenada

	Returns:
		list: lista ordenada
	"""
	for i in range(len(lista), 1, -1):
		trocou = False
		for j in range(i-1):
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]
				trocou = True
				print(lista)
		if not trocou:
			return lista
	return lista
