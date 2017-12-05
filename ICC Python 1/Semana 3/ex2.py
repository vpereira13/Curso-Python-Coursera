"""
Exercícios 2 - FizzBuzz parcial, parte 1

Receba um número inteiro na entrada e imprima

Fizz

se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

def divisivel_3(numero):
	"""Função para verificar se um número é divisivel por 3

	Args:
		numero (int): número a ser analisado

	Returns:
		bool: True, se o número for divisível por 3. Caso contrário, False
	"""
	return True if numero % 3 == 0 else False

if __name__ == "__main__":
	numero = int(input("Digite um número intero: "))

	if divisivel_3(numero):
		print("Fizz")
	else:
		print(numero)
