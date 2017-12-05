"""
Exercício 2: Triângulos semelhantes

Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. Caso negativo, deve devolver False.

Verifique a semelhança dos triângulos através do comprimento dos lados.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

Exemplo:

t1 = Triangulo(2, 2, 2)
t2 = Triangulo(4, 4, 4)
t1.semelhantes(t2)
# deve devolver True
"""

#import pytest # Importar para fazer testes

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

	def tipo_lado(self):
		"""Função para determinar qual o tipo do triângulo a partir
		dos lados dele

		Returns:
		    str: tipo do triângulo (equilátero, isósceles ou escaleno)
		"""
		if self.a == self.b:
			if self.a == self.c:
				return "equilátero"
			else:
				return "isósceles"
		elif self.b == self.c:
			return "isósceles"
		else:
			if self.a == self.c:
				return "isósceles"
			else:
				return "escaleno"

	def retangulo(self):
		"""Função para verificar se o triângulo é retângulo (tem um ângulo
		de 90 graus) ou não

		Returns:
			bool: True se for retângulo e False caso contrário
		"""
		lados = [self.a, self.b, self.c]
		lados.sort()

		return True if lados[2] ** 2 == lados[0] ** 2 + lados[1] ** 2 else False

	def semelhantes(self, triangulo):
		""" Função para verificar semelhança de triângulos

		Args:
			triangulo (Triangulo): uma instância de Triangulo

		Returns:
			bool: True se os triângulos forem semelhantes, False caso contrário
		"""
		razao = self.a/triangulo.a

		return True if razao*triangulo.b == self.b and razao*triangulo.c == self.c else False

"""
# Testes das funções tipo_lado, retangulo e semelhantes

@pytest.fixture
def t(in1, in2, in3):
	return Triangulo(in1, in2, in3)

@pytest.mark.parametrize("in1, in2, in3, esperado",[
	(1, 1, 1, "equilátero"),
	(4, 4, 4, "equilátero"),
	(1, 1, 2, "isósceles"),
	(2, 1, 1, "isósceles"),
	(1, 2, 1, "isósceles"),
	(1, 2, 3, "escaleno"),
	(3, 2, 1, "escaleno")
	])
def testLado(in1, in2, in3, esperado):
	assert t(in1, in2, in3).tipo_lado() == esperado

@pytest.mark.parametrize("in1, in2, in3, esperado",[
	(1, 2, 3, False),
	(3, 4, 5, True),
	(4, 5, 3, True),
	(1, 1, 1, False),
	(1, 2, 3, False),
	(2, 2, 3, False)
	])
def testRetangulo(in1, in2, in3, esperado):
	assert t(in1, in2, in3).retangulo() == esperado

@pytest.mark.parametrize("in1, in2, in3, in4, in5, in6, esperado",[
	(1, 2, 3, 3, 2, 1, False),
	(3, 4, 5, 6, 8, 10, True),
	(4, 5, 3, 2, 2.5, 1.5, True),
	(1, 1, 1, 1, 2, 3, False)
	])
def testSemelhantes(in1, in2, in3, in4, in5, in6, esperado):
	t2 = t(in1, in2, in3)
	assert t(in4, in5, in6).semelhantes(t2) == esperado
"""