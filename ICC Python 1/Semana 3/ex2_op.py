"""
Exercício 2 - Desafio da videoaula

Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros a, b, e c da equação ax2+bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima:

a raiz desta equação é X

onde X é o valor da raiz

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente, ou seja, X deve ser menor que Y.
"""

def delta(a, b, c):
	"""Função para calcular o Delta utilizado na fórmula de Bhaskara,
	delta = b^2 - 4ac

	Args:
		a (float): coeficiente do x^2
		b (float): coeficiente do x^1
		c (float): coeficiente do x^0

	Returns:
		float: valor de delta
	"""
	return b**2 - 4*a*c

def bhaskara(a, b, c):
	"""Função para calcular os valores das raízes, se existirem, da
	equação de segundo grau, dos coeficientes a, b, c. Não retorna os
	valores, só imprime na tela o que foi pedido

	Args:
		a (float): coeficiente do x^2
		b (float): coeficiente do x^1
		c (float): coeficiente do x^0
	"""
	d = delta(a, b, c)
	if d < 0:
		print("esta equação não possui raízes reais")

	else:
		x = (-b+d)/(2*a)
		if d == 0:
			print("a raiz desta equação é", x)
		else:
			x2 = (-b-d)/(2*a)
			print("as raízes da equação são", min(x, x2), "e", max(x, x2))

if __name__ == "__main__":
	a = float(input("Digite o coeficiente a da função: "))
	b = float(input("Digite o coeficiente b da função: "))
	c = float(input("Digite o coeficiente c da função: "))

	bhaskara(a, b, c)