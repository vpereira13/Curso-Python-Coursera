"""
Exercício 1 - Máximo

Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Note que

maximo(3,4) deve devolver 4

maximo(0,-1) deve devolver 0
"""

#import pytest

def maximo(n, m):
	"""Função que retorna o máximo entre dois valores

	Args:
		n (int): valor a ser comparado
		m (int): valor a ser comparado

	Returns:
		int: maior valor entre os dois
	"""
	return n if n > m else m

"""
# Casos de teste

@pytest.mark.parametrize("n, m, esperado",[
	(-123, 1, 1),
	(1, -123, 1),
	(1, 1, 1),
	(-12, -123, -12),
	(123123, 123123123, 123123123),
	(1, 0, 1)
	])
def testMaximo(n, m, esperado):
	assert maximo(n, m) == esperado
"""