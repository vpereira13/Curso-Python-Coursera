"""
Exercício 3

Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:

Exemplo 1:

	Entrada de Dados:

Digite um número inteiro: 78615

	Saída de Dados:

O dígito das dezenas é 1

Exemplo 2:

	Entrada de Dados:

Digite um número inteiro: 2

	Saída de Dados:

O dígito das dezenas é 0

Dica: O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor. O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.
"""

def descobre_dezena(numero):
	"""Função que dado um numero inteiro ele devolve o valor da dezena do mesmo

	Args:
		numero (int): número que deseja descobrir o valor da dezena

	Returns:
		int: valor da dezena do número passado por parametro
	"""
	numero = numero // 10
	dezena = numero % 10

	return dezena

def imprime(dezena):
	"""Função para imprimir do jeito que exercício pede

	Args:
		dezena (int): valor da dezena que tem que ser apresentado como resposta
	"""
	print("O dígito das dezenas é", dezena)

if __name__ == "__main__":
	numero = int(input("Digite um número inteiro: "))
	imprime(descobre_dezena(numero))