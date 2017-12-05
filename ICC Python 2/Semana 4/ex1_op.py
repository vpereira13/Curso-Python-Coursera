"""
Exercício 1: Gerando listas grandes

Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma lista contendo n números inteiros aleatórios.
"""

import random
import sys
#import pytest

def lista_grande(n):
	"""Função para gerar uma lista de tamanho n contendo números
	inteiros aleatórios

	Args:
		n (int): tamanho da lista a ser gerado

	Returns:
		list: lista com n números aleatórios
	"""
	assert n > -1
	lista = []
	for i in range(n):
		lista.append(random.randrange(sys.maxsize))

	return lista

"""
# Casos de teste

@pytest.mark.parametrize("n, esperado",[
	(0, 0)
	(1, 1),
	(4, 4),
	(100, 100),
	(100000, 100000)
	])
def testLista(n, esperado):
	assert len(lista_grande(n)) == esperado
"""