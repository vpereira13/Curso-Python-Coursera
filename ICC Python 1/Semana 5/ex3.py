"""
Exercício 3 - Vogais

Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Note que

vogal("a") deve devolver True

vogal("b") deve devolver False

vogal("E") deve devolver True

Os valores True e False devolvidos devem ser do tipo bool (booleanos)

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.
"""

#import pytest

def vogal(caractere):
	"""Função para verificar se um caracter é vogal ou não

	Args:
		caractere (char): caracter a ser analisado

	Returns:
		bool: True, se for vogal. False, se for consoante
	"""
	return True if caractere in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] else False


"""
# Casos de teste

@pytest.mark.parametrize("caracter, esperado",[
	("a", True),
	("e", True),
	("i", True),
	("o", True),
	("u", True),
	("A", True),
	("E", True),
	("I", True),
	("O", True),
	("U", True),
	("b", False),
	("c", False),
	("C", False),
	("D", False),
	(" ", False)
	])
def testVogal(caracter, esperado):
	assert vogal(caracter) == esperado
"""