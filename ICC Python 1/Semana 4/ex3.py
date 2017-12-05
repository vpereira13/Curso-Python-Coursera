"""
Exercício 3

Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Digite um número inteiro: 123
6

Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.
"""

def soma_dos_digitos(n):
	"""Função para calcular a soma de todos os dígitos de um número inteiro

	Args:
	    n (int): número inteiro a ser calculado a soma

	Returns:
	    int: soma de todos os dígitos de um número
	"""
	valor = 0

	while n != 0:
		valor += n % 10
		n //= 10

	return valor

if __name__ == '__main__':
	n = int(input("Digite um número inteiro: "))

	print(str(soma_dos_digitos(n)))