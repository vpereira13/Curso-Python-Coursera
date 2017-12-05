"""
Exercício 2

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
#        #
##########

digite a largura: 2
digite a altura: 2
##
##
"""

def imprime_retangulo(altura, largura):
	"""Função para imprimir um retângulo composto por #
	na borda e vazio por dentro, dada uma altura e uma largura

	Args:
		altura (int): altura do retângulo
		largura (int): largura do retângulo
	"""
	for i in range(altura):
		for j in range(largura):
			if i == 0 or i == altura - 1:
				print("#", end="")
			else:
				if j == 0 or j == largura - 1:
					print("#", end="")
				else:
					print(" ", end="")
		print()

if __name__ == '__main__':
	largura = int(input("digite a largura: "))
	altura = int(input("digite a altura: "))

	imprime_retangulo(altura, largura)