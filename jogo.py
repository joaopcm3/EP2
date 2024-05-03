##############################
######## CONSTANTES #########
##############################

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

def posicao_suporta(mapa_tab,num_blocos,li,col,alocacao):
    
    for i in range(num_blocos):

        if alocacao == 'h':

            if li >= len(mapa_tab) or col + i >= len(mapa_tab[li]):
                return False
            
            elif mapa_tab[li][col + i] == 'N':
                return False

        elif alocacao == 'v':

            if li + i >= len(mapa_tab) or col >= len(mapa_tab[li + i]):
                return False

            elif mapa_tab[li + i][col] == 'N':
                return False

    return True

########### Alocando navios para o computador ####################

import random

##### Chamando função novamente #####

def posicao_suporta(mapa_tab,num_blocos,li,col,alocacao):
    
    for i in range(num_blocos):

        if alocacao == 'h':

            if li >= len(mapa_tab) or col + i >= len(mapa_tab[li]):
                return False
            
            elif mapa_tab[li][col + i] == 'N':
                return False

        elif alocacao == 'v':

            if li + i >= len(mapa_tab) or col >= len(mapa_tab[li + i]):
                return False

            elif mapa_tab[li + i][col] == 'N':
                return False

    return True

#####################################

def aloca_navios(mapa_alocacao,lista_blocos):

    for j in lista_blocos:
        dps = False
        while dps == False:
            n = len(mapa_alocacao)
            li = random.randint(0, n-1)
            col = random.randint(0, n-1)
            alocacao = random.choice(['h', 'v'])
            dps = posicao_suporta(mapa_alocacao,j,li,col,alocacao)
        for i in range (j):
            if alocacao == 'v':
                mapa_alocacao[li + i][col] = 'N'
            elif alocacao == 'h':
                mapa_alocacao[li][col + i] = 'N'
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

##### BIBLIOTECA PARA TEMPO #####

import time

###### Espaçamento para mapa (função) ######

def espacamento(n):
    lista = []
    contador_externo = 0
    
    while contador_externo < n:
        contador_interno = 0
        l = ['   '] * n
        lista.append(l)
        contador_externo += 1

    return lista

### ESCOLHA DO PAÍS DO COMP ###

paises = ['Brasil', 'França', 'Austrália', 'Rússia', 'Japão']
num_p = ['1', '2', '3', '4', '5']
mapa = cria_mapa(10)
barco_comp = []
pais_comp = random.choice(paises)

while pais_comp not in PAISES:
    pais_comp = random.choice(paises)

barcos_do_pais = PAISES[pais_comp]
for barco in barcos_do_pais:
    quantidade = barcos_do_pais[barco]
    i = 0
    while i < quantidade:
        barco_comp.append(CONFIGURACAO[barco])
        i += 1

mapa_comp = aloca_navios(mapa, barco_comp)