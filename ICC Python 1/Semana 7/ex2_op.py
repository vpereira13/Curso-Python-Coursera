"""
Exercício 2 - (Difícil) Soma das hipotenusas

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

Exemplo:

# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
soma_hipotenusas(25)
# deve devolver 105
"""

def eh_hipotenusa(n):
	"""Função para verificar se um valor inteiro pode
	ser uma hipotenusa

	Args:
		n (int): valor a ser analisado

	Returns:
		bool: True, se for hipotenusa. False, se caso não for
	"""
	for i in range(1, n):
		for j in range(1, n):
			if i**2 + j**2 == n**2:
				return True
	return False

def soma_hipotenusas(n):
	"""Função que calcula a soma de todas as hipotenusas
	de valor inteiro

	Args:
		n (int): tamanho máximo da hipotenusa

	Returns:
		int: soma de todas as hipotenusas de um até o valor dado
	"""
	soma = 0

	for i in range(1, n+1):
		if eh_hipotenusa(i):
			soma += i

	return soma
