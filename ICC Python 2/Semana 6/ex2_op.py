"""
Implemente a função fatorial(x), que recebe como parâmetro um número inteiro e devolve um número inteiro correspondente ao fatorial de x.

Sua solução deve ser implementada utilizando recursão.
"""

def fatorial(n):
	"""Função recursiva que calcula o fatorial de um certo número

	Args:
		n (int): número a ser computado

	Returns:
		int: valor do fatorial
	"""
	if n < 2:
		return 1
	else:
		return n * fatorial(n-1)

"""
# Casos de teste

import pytest

@pytest.mark.parametrize("entrada, esperado",[
	(0, 1),
	(1, 1),
	(2, 2),
	(5, 120),
	(10, 3628800)
	])

def testFatorial(entrada, esperado):
	assert fatorial(entrada) == esperado
"""