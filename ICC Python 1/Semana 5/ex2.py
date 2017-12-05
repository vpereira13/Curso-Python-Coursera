"""
Exercício 2 - Primos

Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Note que

maior_primo(100) deve devolver 97

maior_primo(7) deve devolver 7

Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.
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

def maior_primo(n):
	"""Função para achar o maior número primo menor ou igual ao passado por parâmetro

	Args:
		n (int): número inteiro a ser analisado

	Returns:
		int: maior número primo menor ou igual ao passado por parâmetro
	"""
	assert n >= 2

	while not eh_primo(n):
		n -= 1

	return n

"""
# Casos de teste

@pytest.mark.parametrize("n, esperado",[
	(2, 2),
	(6, 5),
	(100, 97),
	(7, 7),
	(10000, 9973)
	])
def testMaiorPrimo(n, esperado):
	assert maior_primo(n) == esperado
"""