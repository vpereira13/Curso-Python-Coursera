"""
Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

Exemplo:

Digite o valor de n: 5
1
3
5
7
9
"""

if __name__ == '__main__':
	n = int(input("Digite o valor de n: "))

	for i in range(n):
		print(str(i*2 + 1))
