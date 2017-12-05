"""
Exercícios 3 - FizzBuzz parcial, parte 2

Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

def divisivel_5(numero):
	"""Função para verificar se um número é divisível por 5

	Args:
		numero (int): número a ser analisado

	Returns:
		bool: True, se o número for divisível por 5, caso contrário False
	"""
	return True if numero % 5 == 0 else False

if __name__ == "__main__":
	numero = int(input("Digite um número inteiro: "))
	if divisivel_5(numero):
		print("Buzz")
	else:
		print(numero)
