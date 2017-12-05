"""
Exercício 1: Uma classe para triângulos

Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.

t = Triangulo(1, 1, 1)
# deve atribuir uma referência para um triângulo de lados 1, 1 e 1 à variável t

Um objeto desta classe deve responder às seguintes chamadas:

t.a
# deve devolver o valor do lado a do triângulo
t. b
# deve devolver o valor do lado b do triângulo
t.c
# deve devolver o valor do lado c do triângulo

t.perimetro()
# deve devolver um inteiro correspondente ao valor do perímetro do triângulo.
"""

class Triangulo():
	"""Classe Triângulo, figura geométrica de três lados

	Attributes:
		a (int/float): valor de um lado do triângulo
		b (int/float): valor de um lado do triângulo
		c (int/float): valor de um lado do triângulo
	"""
	def __init__(self, a, b, c):
		"""Construtor da classe Triangulo, passando os lados por parâmetro

		Args:
			a (int/float): valor de um lado do triângulo
			b (int/float): valor de um lado do triângulo
			c (int/float): valor de um lado do triângulo
		"""
		self.a = a
		self.b = b
		self.c = c

	def perimetro(self):
		"""Função para retornar o perímetro do triângulo

		Returns:
			int: soma de todos os lados do triângulo
		"""
		return self.a + self.b + self.c
