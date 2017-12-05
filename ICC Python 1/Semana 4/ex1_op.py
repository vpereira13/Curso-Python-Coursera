"""
Exercício 1

Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 11

primo

Digite um número inteiro: 12

não primo
"""

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

if __name__ == '__main__':
	n = int(input("Digite um número inteiro: "))

	if eh_primo(n):
		print("primo")
	else:
		print("não primo")