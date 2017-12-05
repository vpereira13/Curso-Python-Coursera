"""
Exercícios 4 - FizzBuzz parcial, parte 3

Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

def divisivel_15(numero):
	"""Função para verificar se um número é divisível por 3 e por 5,
	ou seja, divisível por 15

	Args:
		numero (int): número a ser analisado

	Returns:
		bool: True, se o número for divisível por 3 e 5, caso contrário False
	"""
	return True if numero % 15 == 0 else False

if __name__ == "__main__":
	numero = int(input("Digite um número inteiro: "))
	if divisivel_15(numero):
		print("FizzBuzz")
	else:
		print(numero)
