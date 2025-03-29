#   Made by:                                    Data: 
#           Diego Silva Cortez                       27/03/2025
#                                               
#
#   Programa que recebe um nome de arquivo que contém uma matriz, a lê e a transforma
#   num array np. Por fim ela imprime na tela, e salva em um arquivo .txt, o nome do arquivo aberto e a dimensão
#   da matriz.

from funcoes import criaMatriz
from funcoes import saida

arquivo = input("Nome do arquivo:")
print()
matriz = criaMatriz.carregaDados(arquivo)

saida.imprime(matriz, arquivo)
saida.salvaRes(matriz, arquivo)