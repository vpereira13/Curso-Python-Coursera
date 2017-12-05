"""
Exercício 1 - FizzBuzz

Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso a função não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

Note que

fizzbuzz(3) deve devolver Fizz

fizzbuzz(5) deve devolver Buzz

fizzbuzz(15) deve devolver FizzBuzz

fizzbuzz(4) deve devolver 4

As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e minúsculas
"""

#import pytest

def fizzbuzz(n):
	"""Função para verificar se um número é divisível por 3 e por 5

	Args:
		n (int): número inteiro a ser analisado

	Returns:
		str/int: se divisível por 3 e não por 5, "Fizz"
		se divisível por 5 e não por 3, "Buzz"
		se divisível por 3 e 5, "FizzBuzz"
		n se não for divisível por 3 nem por 5
	"""
	if n % 3 == 0:
		if n % 5 == 0:
			return "FizzBuzz"
		else:
			return "Fizz"
	else:
		if n % 5 == 0:
			return "Buzz"
		else:
			return n

"""
# Casos de teste

@pytest.mark.parametrize("n, esperado",[
	(1, 1),
	(3, "Fizz"),
	(9, "Fizz"),
	(-15, "FizzBuzz"),
	(5, "Buzz"),
	(-25, "Buzz"),
	(-23, -23),
	(4, 4)
	])
def testFizzBuzz(n, esperado):
	assert fizzbuzz(n) == esperado
"""