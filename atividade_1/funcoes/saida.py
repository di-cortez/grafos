#funcão que imprime na tela o nome do arquivo e as dimensão da matriz
def imprime(matriz, nomeArq):
    print(f"Nome da instância: {nomeArq}\n")
    lin, col = matriz.shape
    print(f"Número de linhas: {lin}\nNúmero de colunas: {col}")
    return

#funcao que salva em um arquivo tipo txt o nome do arquivo aberto e as dimensões
# da matriz contida nele.
def salvaRes(matriz, nomeArq):
    lin, col = matriz.shape
    caminho = f'/home/diego/3_semestre/grafos/atividade_1/resultados/{nomeArq}_res.txt'
    arq = open(caminho, 'a+')
    arq.writelines(f"Dataset: {nomeArq}\n")
    arq.writelines(f"Shape: ({lin},{col})\n")
    arq.close()
    return
