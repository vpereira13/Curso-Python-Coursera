"""
Exercício 1

Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

	Olá, Fulano de Tal
	A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

	Entrada de Dados:
		Digite o nome do cliente: Fulano de Tal
		Digite o dia de vencimento: 9
		Digite o mês de vencimento: Janeiro
		Digite o valor da fatura: 350,00

	Saída de Dados:
		Olá, Fulano de Tal
		A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
"""

def coleta_dados():
	"""Função para coletar os dados do cliente e de sua fatura

	Returns:
		tuple: Uma tupla contendo  nome do cliente, dia da fatura,
		mes da fatura e valor da fatura, respectivamente
	"""
	nome = input("Digite o nome do cliente: ")
	dia = input("Digite o dia de vencimento: ")
	mes = input("Digite o mês de vencimento: ")
	valor = input("Digite o valor da fatura: ")

	return (nome, dia, mes, valor)

NOME = 0
DIA = 1
MES = 2
VALOR = 3

def imprime_fatura(tupla):
	"""Função para imprimir a mensagem para os clientes, com as informações
	passadas por parametros

	Args:
		tupla (tuple): Uma tupla contendo nome do cliente, dia da fatura,
		mes da fatura e valor da fatura, respectivamente
	"""
	print("Olá,", tupla[NOME])
	print("A sua fatura com vencimento em", tupla[DIA], "de", tupla[MES], "no valor de R$", tupla[VALOR], "está fechada." )

if __name__ == "__main__":
	imprime_fatura(coleta_dados())