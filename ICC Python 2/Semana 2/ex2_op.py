"""
Exercício 2: Ordem lexicográfica

Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.

Exemplos:

primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'
"""

def primeiro_lex(lista):
	"""Função para retornar a primeira string dada a ordem lexicográfica

	Args:
	    lista (list): lista de strings, pode conter letras maiúsculas
	    e minúsculas

	Returns:
	    str: a primeira string da lista segundo a ordem lexicográfica
	"""
	lista.sort()

	return lista[0]
