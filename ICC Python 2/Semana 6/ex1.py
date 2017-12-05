"""
Exercício 1: Soma dos elementos de uma lista

Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.

Sua solução deve ser implementada utilizando recursão.
"""

def soma_lista(lista):
	"""Função recursiva que calcula a soma dos elementos de uma lista

	Args:
	    lista (list): lista de números inteiros

	Returns:
	    int: se tamanho da lista = 1, retorna o único valor, caso contrário, retorna
	    o primeiro elemento mais a chamada de função com a lista restante
	"""
	if len(lista) < 2:
		return lista[0]
	else:
		return lista[0] + soma_lista(lista[1:])

"""
# Casos de teste

import pytest

@pytest.mark.parametrize("entrada, esperado",[
	([1,2,3,4,5,6,7], 28),
	([0,0,0,0,0,0,0], 0),
	([-1,2,3,10,-7,1], 8),
	([-1,-1,-1,-1,-1,-1,-1], -7)
	])
def testa_soma(entrada, esperado):
	assert soma_lista(entrada) == esperado
"""