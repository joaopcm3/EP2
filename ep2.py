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

##### Chamando função novamente #####

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

#####################################

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

##############################
######## INFORMAÇÔES #########
##############################

# Black: \u001b[30m
# Red: \u001b[31m
# Green: \u001b[32m
# Yellow: \u001b[33m
# Blue: \u001b[34m
# Magenta: \u001b[35m
# Cyan: \u001b[36m
# White: \u001b[37m
# Reset: \u001b[0m

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}
 
alfabeto_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
alfabeto = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

##############################

############
### JOGO ###
############