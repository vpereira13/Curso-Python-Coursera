"""
Exercício 2: Tipos de triângulos

Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isóceles.

Exemplos:

t = Triangulo(4, 4, 4)
t.tipo_lado()
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5)
.tipo_lado()
# deve devolver 'escaleno'
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

"""
Parte de teste, treinando e testando ;D

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
def testlado(in1, in2, in3, esperado):
	assert t(in1, in2, in3).tipo_lado() == esperado
"""