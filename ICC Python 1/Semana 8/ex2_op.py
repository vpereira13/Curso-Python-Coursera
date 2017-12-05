"""
Exercício 2 - Invertendo sequência

Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros terminados por 0 e imprima todos os valores em ordem inversa. Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:

Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1
"""

def imprime_inverso(lista):
	"""Função que imprime um item por linha na seguinte ordem,
	de trás para frente

	Args:
		lista (list): lista de números inteiros
	"""
	for i in range(len(lista)-1, -1, -1):
		print(lista[i])

if __name__ == '__main__':
	lista = []

	valor = int(input("Digite um número: "))

	while valor != 0:
		lista.append(valor)
		valor = int(input("Digite um número: "))

	imprime_inverso(lista)
