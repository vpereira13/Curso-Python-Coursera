"""
Exercício 1 - Primos

Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
"""

#import pytest

def eh_primo(n):
	"""Função para checar se um número é primo

	Args:
		n (int): número a ser analisado

	Returns:
		bool: True, se for primo e False, se não for primo
	"""
	for i in range(2, n//2 + 1):
		if n % i == 0:
			return False
	return True

def n_primos(n):
	"""Função para descobrir quantos primos tem do número de
	entrada (inclusive) até o número 2 (inclusive)

	Args:
	    n (int): número a ser analisado

	Returns:
	    int: número de números primos entre o número de entrada
	    até o dois
	"""
	assert n > 1
	contador = 0

	for i in range(n, 1, -1):
		if eh_primo(i):
			contador += 1

	return contador

"""
#Casos de teste

@pytest.mark.parametrize("entrada, esperado",[
	(6,3),
	(15,6),
	(20,8),
	(24,9)
	])

def testPrimos(entrada, esperado):
	assert n_primos(entrada) == esperado
"""