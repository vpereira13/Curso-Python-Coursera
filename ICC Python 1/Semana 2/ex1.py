"""
Exercício 1

Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:
		Entrada de Dados:

	Digite o valor correspondente ao lado de um quadrado: 3

		Saída de Dados:

	perímetro: 12 - área: 9
"""

def calcula_perimetro(lado):
	"""Função que dado o tamanho do lado de um quadrado,
	retorna o perímetro do mesmo

	Args:
		lado (int): tamanho do lado de um quadrado

	Returns:
		int: perímetro de um quadrado
	"""
	if lado > 0:
		perimetro  = 4 * lado

		return perimetro

def calcula_area(lado):
	"""Função que dado o tamanho do lado de um quadrado,
		retorna a área do mesmo

	Args:
		lado (int): tamanho do lado de um quadrado

	Returns:
		int: área de um quadrado
	"""
	if lado > 0:
		area = lado * lado

		return area

if __name__ == "__main__":
	lado = int(input("Entre com o valor do lado de um quadrado: "))

	print("perímetro:", calcula_perimetro(lado), "- área:", calcula_area(lado))