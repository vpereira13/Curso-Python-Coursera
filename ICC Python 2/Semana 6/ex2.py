"""
Exercício 2: Encontrando ímpares em uma lista

Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
"""

def encontra_impares(lista):
	"""Função que dada uma lista de números inteiros, encontra todos os números
	ímpares recursivamente

	Args:
		lista (list): lista de interos

	Returns:
		list: lista contendo somente números ímpares + chamada recursiva
	"""
	l = []
	if len(lista) < 1:
		return l
	else:
		numero = lista.pop()
		if numero % 2 != 0:
			l.append(numero)
		return l + (encontra_impares(lista))

"""
# Casos de teste

import pytest

@pytest.mark.parametrize("entrada, esperado",[
	([1,2,3,4,5,6,7,8,9,0],[9,7,5,3,1]),
	([2,4,6,8,0],[]),
	([1,9],[9,1]),
	([],[]),
	([1,1,1,1,1],[1,1,1,1,1])
	])

def testImpares(entrada, esperado):
	assert encontra_impares(entrada) == esperado
"""