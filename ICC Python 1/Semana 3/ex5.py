"""
Exercício 5 - Verificando ordenação

Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
"""

def verifica_crescente(a, b, c):
	"""Função para verificar se os números passados por parâmetros
	estão em ordem crescente ou não.

	Args:
		a (int): primeiro número da sequência
		b (int): segundo número da sequência
		c (int): terceiro número da sequência

	Returns:
		bool: True se a sequência estiver em ordem crecente, caso contrário
		False
	"""
	return True if a <= b and b <= c else False

if __name__ == "__main__":
	a = int(input("Digite o primeiro número: "))
	b = int(input("Digite o segundo número: "))
	c = int(input("Digite o terceiro número: "))

	print("crescente") if verifica_crescente(a, b, c) else print("não está em ordem crescente")