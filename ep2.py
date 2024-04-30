###############
### FUNÇÔES ###
###############

########### Cria matriz quadradadas de espaços ####################

def cria_mapa(N):  
    lista = []

    for i in range(N):
        m = [' ']*N
        lista.append(m)
    return lista

########### Navio pode ser alocado na posição ####################

def posicao_suporta(mapa_tab,num_blocos,linha,coluna,alocacao):
    
    for i in range(num_blocos):

        if alocacao == 'h':

            if linha >= len(mapa_tab) or coluna + i >= len(mapa_tab[linha]):
                return False
            
            elif mapa_tab[linha][coluna + i] == 'N':
                return False

        elif alocacao == 'v':

            if linha + i >= len(mapa_tab) or coluna >= len(mapa_tab[linha + i]):
                return False

            elif mapa_tab[linha + i][coluna] == 'N':
                return False

    return True

########### Alocando navios para o computador ####################

import random

def aloca_navios(mapa_alocacao,lista_blocos):

    for j in lista_blocos:
        dps = False
        while dps == False:
            n = len(mapa_alocacao)
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            alocacao = random.choice(['h', 'v'])
            dps = posicao_suporta(mapa_alocacao,j,linha,coluna,alocacao)
        for i in range (j):
            if alocacao == 'v':
                mapa_alocacao[linha + i][coluna] = 'N'
            elif alocacao == 'h':
                mapa_alocacao[linha][coluna + i] = 'N'
    return mapa_alocacao

########### Verificando se acabou os 'N's da matriz ####################

def foi_derrotado(matriz):

    for lista in matriz:
        for caracter in lista:
            if caracter == 'N':
                return False
    
    return True

############
### JOGO ###
############

