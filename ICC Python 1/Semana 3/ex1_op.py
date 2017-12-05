"""
Exercício 1 - Distância entre dois pontos

Receba 4 números inteiros na entrada. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto
"""

from math import sqrt

X1 = 0
Y1 = 1
X2 = 2
Y2 = 3

def calcula_distancia(pontos):
	"""Função para calcular a distância entre dois pontos, num plano cartesiano

	Args:
		pontos (list): uma lista contendo x1, y1, x2 e y2 respectivamente

	Returns:
		float: valor da distância euclidiana entre dois pontos
	"""
	return sqrt(((pontos[X1] - pontos[X2]) ** 2) + ((pontos[Y1] - pontos[Y2]) ** 2))

if __name__ == "__main__":
	x1 = int(input("Digite o valor do ponto x1: "))
	y1 = int(input("Digite o valor do ponto y1: "))
	x2 = int(input("Digite o valor do ponto x2: "))
	y2 = int(input("Digite o valor do ponto y2: "))

	pontos = [x1, y1, x2, y2]

	print("longe") if calcula_distancia(pontos) >= 10 else print("perto")