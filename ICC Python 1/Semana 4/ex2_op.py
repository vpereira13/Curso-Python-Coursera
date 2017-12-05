"""
Exercício 2 - Desafio do vídeo "Repetição com while"

Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 123

não

Digite um número inteiro: 3556

sim
"""

def adjacente(n):
	"""Função para verificar se dado um número inteiro há dígitos adjacentes iguais

	Args:
	    n (int): número a ser analisado

	Returns:
	    bool: True, se há valores adjacentes iguais e False se não houver
	"""
	while n != 0:
		valor1 = n % 10
		valor2 = (n % 100)//10
		if valor1 == valor2:
			return True
		n //= 10

	return False

if __name__ == '__main__':
	n = int(input("Digite um número inteiro: "))

	if adjacente(n):
		print("sim")
	else:
		print("não")