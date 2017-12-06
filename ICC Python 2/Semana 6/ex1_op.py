"""
Exercício 1: Fibonacci

Implemente a função fibonacci(n), que recebe como parâmetro um número inteiro e devolve um número inteiro correspondente ao n-ésimo elemento da sequência de Fibonacci. Sua solução deve ser implementada utilizando recursão.

Exemplo:

fibonacci(4)
# deve devolver => 3
fibonacci(2)
# deve devolver => 1
"""

def fibonacci(n):
	"""Função recursiva que retorna o n-ésimo elemento da sequência de
	fibonacci

	Args:
		n (int): número a ser computado

	Returns:
		int: chamada recursiva com n-1 + chamada recursiva com (n-2)
	"""
	if n < 2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

"""
# Casos de teste

import pytest

@pytest.mark.parametrize("entrada, esperado",[
	(4, 3),
	(2, 1),
	(8, 21),
	(12, 144)
	])

def testFibonacci(entrada, esperado):
	assert fibonacci(entrada) == esperado
"""