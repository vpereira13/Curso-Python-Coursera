"""
Exercício 2

Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

	Entrada de Dados:

Por favor, entre com o número de segundos que deseja converter: 178615

	Saída de Dados:

2 dias, 1 horas, 36 minutos e 55 segundos.
"""

DIA = 86400
HORA = 3600
MIN = 60

def converte_tempo(segundos):
	"""Função que converte uma certa quantidade de segundos passada por
	parametro em dias, horas, minutos e segundos

	Args:
		segundos (int): quantidade em segundos para converter

	Returns:
		tuple: uma tupla contendo a quantidade de dias, horas, minutos
		e segundos, respectivamente
	"""
	dias = segundos // DIA
	segundos = segundos % DIA

	horas = segundos // HORA
	segundos = segundos % HORA

	minutos = segundos // MIN
	segundos = segundos % MIN

	return (dias, horas, minutos, segundos)

idDia = 0
idHr = 1
idMin = 2
idSeg = 3

def imprime_tempo(tupla):
	"""Função para imprimir da maneira correta os dias, horas, minutos e segundos
	passados por parâmetro

	Args:
		tupla (tuple of int): uma tupla contendo dias, horas, minutos e segundos,
		respectivamente
	"""
	print(str(tupla[idDia]), "dias,", str(tupla[idHr]), "horas,",
		str(tupla[idMin]), "minutos e", str(tupla[idSeg]), "segundos.")

if __name__ == "__main__":
	segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
	imprime_tempo(converte_tempo(segundos))