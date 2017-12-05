"""
Exercício 2 - Máximo com 3 parâmetros

Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

Note que

maximo(30,14,10) deve devolver 30

maximo(0,-1, 1) deve devolver 1
"""

#import pytest

def maximo(a, b, c):
	"""Função para comparar três números inteiros e devolver o maior entre eles

	Args:
		a (int): valor a ser comparado
		b (int): valor a ser comparado
		c (int): valor a ser comparado

	Returns:
		int: maior valor entre os três números passados por parametros
	"""
	if a > b:
		if a > c:
			return a
		else:
			return c
	elif b > c:
		return b
	else:
		return c

"""
# Casos de teste

@pytest.mark.parametrize("a, b, c, esperado",[
	(1, 1, 1, 1),
	(0, 1, 2, 2),
	(2, 1, -1, 2),
	(2, -1, 1, 2),
	(1, 2, -1, 2),
	(1, 3, 2, 3),
	(0, -3, 4, 4)
	])
def testMaximo(a, b, c, esperado):
	assert maximo(a, b, c) == esperado
"""