"""
Exercício 1 - Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
"""

def remove_repetidos(lista):
	"""Função que remove os elementos repetidos de uma lista

	Args:
		lista (list): lista a ser operada

	Returns:
		list: lista sem elementos repetidos
	"""
	lista.sort()
	pivo = lista[0]
	i = 1
	while i < len(lista):
		if pivo == lista[i]:
			lista.remove(lista[i])
		else:
			pivo = lista[i]
			i += 1

	return lista
