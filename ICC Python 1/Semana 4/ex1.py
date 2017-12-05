"""
Exercício 1

Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

Exemplo:

Digite o valor de n: 5
120
"""

#import pytest

def fatorial(n):
	"""Função para calcular o fatorial de um certo número

	Args:
	    n (int): valor de entrada para ser calculado o fatorial

	Returns:
	    int: fatorial do valor de entrada
	"""
	if n < 2:
		return 1
	else:
		return n * fatorial(n - 1)

if __name__ == '__main__':
	n = int(input("Digite o valor de n: "))

	print(str(fatorial(n)))

"""
@pytest.mark.parametrize("entrada, esperado",[
	(0, 1),
	(1, 1),
	(2, 2),
	(3, 6),
	(5, 120)
	])
def testFatorial(entrada, esperado):
	assert fatorial(entrada) == esperado
"""