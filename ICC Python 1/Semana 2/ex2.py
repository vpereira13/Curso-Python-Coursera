"""
Exercício 2

Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:
		Entrada de Dados:

	Digite a primeira nota: 4

	Digite a segunda nota: 5

	Digite a terceira nota: 6

	Digite a quarta nota: 7

		Saída de Dados:

	A média aritmética é 5.5

Attributes:
	QUANTIDADE (int): Description
"""

QUANTIDADE = 4

def calcula_media(n):
	"""Função que dada uma certa quantidade de entradas calcula
	e retorna a média aritmética delas

	Args:
		n (int): quantidade de valores de entrada

	Returns:
		float: média aritmética dos valores de entrada
	"""
	soma_de_notas = 0

	for i in range(n):
		soma_de_notas += int(input("Digite a nota " + str(i+1) + ": "))

	return soma_de_notas/n

if __name__ == "__main__":
	print("A média aritmética é", calcula_media(QUANTIDADE))