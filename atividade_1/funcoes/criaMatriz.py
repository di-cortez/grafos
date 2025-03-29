import numpy as np

#funcao que lê o dataset e cria uma um array do tipo Numpy
def carregaDados(inst):
    caminho = f'/home/diego/3_semestre/grafos/atividade_1/dados/{inst}.txt'
    matriz = np.loadtxt(caminho, dtype='int32', delimiter = " ")
    return matriz
