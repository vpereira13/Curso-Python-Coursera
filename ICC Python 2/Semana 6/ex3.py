"""
Exercício 3: Elefantes

Este exercício tem duas partes:

	Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia. Essa função deve ser implementada utilizando recursão.
	Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1, a função deve devolver uma string vazia. Essa função também deve ser implementada utilizando recursão.

Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+". Lembre-se também que é possível transformar números em strings com a função str().

Dica: Será que neste caso a base da recursão é diferente de n==1?

Por exemplo, uma chamada a elefantes(4) deve devolver uma string contendo:

Um elefante incomoda muita gente
2 elefantes incomodam incomodam muito mais
2 elefantes incomodam muita gente
3 elefantes incomodam incomodam incomodam muito mais
3 elefantes incomodam muita gente
4 elefantes incomodam incomodam incomodam incomodam muito mais
"""

def incomodam(n):
	"""Função que retorna recursivamente uma string contendo n vezes
	a palavra incomodam

	Args:
		n (int): número de vezes que a palavra incomodam será repetida

	Returns:
		str: string "incomodam " + chamada recursiva
	"""
	if n < 1:
		return ""
	else:
		return "incomodam " + incomodam(n-1)

def elefantes(n):
	"""Função que retorna recursivamente a música dos elefantes, a qual vai
	até o n de entrada

	Args:
		n (int): número de iterações que vai ter a música

	Returns:
		str: chamada recursiva + string contendo a primeira parte da música
		com n-1 e segunda parte da musica com n
	"""
	if n < 2:
		if n == 1:
			return "Um elefante incomoda muita gente\n"
		else:
			return ""
	else:
		if n == 2:
			return elefantes(n-1) + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
		else:
			return  elefantes(n-1) + str(n-1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"

"""
# Casos de teste

import pytest

@pytest.mark.parametrize("entrada, esperado",[
	(4, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n3 elefantes incomodam muita gente\n4 elefantes incomodam incomodam incomodam incomodam muito mais\n"),
	(3, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n"),
	(2, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n"),
	(1, "Um elefante incomoda muita gente\n"),
	(0, "")
	])

def testElefantes(entrada, esperado):
	assert elefantes(entrada) == esperado
"""