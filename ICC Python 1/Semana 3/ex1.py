"""
Exercício 1 - Par ou ímpar?

Receba um número inteiro na entrada e imprima

par

quando o número for par ou

ímpar

quando o número for ímpar.
"""

def eh_par(numero):
	"""Função para saber se um certo número é par ou não

	Args:
		numero (int): número a ser analisado

	Returns:
		bool: True, se for par. False, se for ímpar
	"""
	return True if numero % 2 == 0 else False

if __name__ == "__main__":
	if eh_par(int(input("EDigite um número inteiro: "))):
		print("par")
	else:
		print("ímpar")