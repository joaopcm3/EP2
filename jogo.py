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

###############
#### JOGO #####
###############

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

#### ESCOLHA DO PAÍS DO COMP ####

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

### ENTRADA DO JOGO ###

entrada = ''' ===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= '''

alerta = f'Iniciando o jogo!\n\nComputador está alocando os navios de guerra do país {pais_comp}...\nComputador já está em posição de batalha!'

info = '''
1: Brasil
   1 cruzador
   2 torpedeiro
   1 destroyer
   1 couracado
   1 porta-avioes

2: França
   3 cruzador
   1 porta-avioes
   1 destroyer
   1 submarino
   1 couracado

3: Austrália
   1 couracado
   3 cruzador
   1 submarino
   1 porta-avioes
   1 torpedeiro

4: Rússia
   1 cruzador
   1 porta-avioes
   2 couracado
   1 destroyer
   1 submarino

5: Japão
   2 torpedeiro
   1 cruzador
   2 destroyer
   1 couracado
   1 submarino
'''

print(f'{entrada}\n\n{alerta}\n{info}')

##### ESCOLHA DO PAÍS DO PLAYER #####

player = input('Qual o número da nação da sua frota? ')

while player not in num_p:

    print('Opção inválida')
    player = input('Qual o número da nação da sua frota? ')

print(f'Você escolheu a nação {paises[int(player)-1]}\nAgora é sua vez de colocar seus navios de guerra!')
player_pais = paises[int(player)-1]

espaco = '▓▓▓'

##### CRIAÇÃO DE MAPA #####

aparencia_player = espacamento(10)
aparencia_comp = espacamento(10)
player_map = cria_mapa(10)

colocar = []
barcos_do_pais = PAISES[player_pais]
for barco in barcos_do_pais:
    quantidade = barcos_do_pais[barco]
    i = 0
    while i < quantidade:
        colocar.append(barco)
        i += 1

### REPETIÇÃO DE BARCOS (LOOP) ###

for i in range(len(colocar)):

    exibicao = [f'''  COMPUTADOR - {pais_comp}                   JOGADOR - {player_pais}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
    for i in range(9):

        exibicao.append(f'  {i+1} {aparencia_comp[i][0]}{aparencia_comp[i][1]}{aparencia_comp[i][2]}{aparencia_comp[i][3]}{aparencia_comp[i][4]}{aparencia_comp[i][5]}{aparencia_comp[i][6]}{aparencia_comp[i][7]}{aparencia_comp[i][8]}{aparencia_comp[i][9]} {i+1}    {i+1} {aparencia_player[i][0]}{aparencia_player[i][1]}{aparencia_player[i][2]}{aparencia_player[i][3]}{aparencia_player[i][4]}{aparencia_player[i][5]}{aparencia_player[i][6]}{aparencia_player[i][7]}{aparencia_player[i][8]}{aparencia_player[i][9]} {i+1}')
    
    i+=1

    exibicao.append(f' 10 {aparencia_comp[i][0]}{aparencia_comp[i][1]}{aparencia_comp[i][2]}{aparencia_comp[i][3]}{aparencia_comp[i][4]}{aparencia_comp[i][5]}{aparencia_comp[i][6]}{aparencia_comp[i][7]}{aparencia_comp[i][8]}{aparencia_comp[i][9]} 10  10 {aparencia_player[i][0]}{aparencia_player[i][1]}{aparencia_player[i][2]}{aparencia_player[i][3]}{aparencia_player[i][4]}{aparencia_player[i][5]}{aparencia_player[i][6]}{aparencia_player[i][7]}{aparencia_player[i][8]}{aparencia_player[i][9]} 10')
    exibicao.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
    
    for x in exibicao:
        print(x)

#####################################################

    cubo = CONFIGURACAO[colocar[0]]

    print(f'Alocar: {colocar[0]} ({cubo} blocos)')
    
    del colocar[0]
    if len(colocar) > 0:
        perto = colocar[0]
    
        for i in range(1,len(colocar)):
            perto += ', ' + colocar[i]
    
        print(f'Próximos: {perto}')

    posicao = False

    while posicao == False:

        t = False

        while t == False:

            le = input('Informe a letra: ')
            le = le.upper()

            if le not in alfabeto:
                print('Letra inválida')

            else:
                t = True
        
        t = False

        while t == False:

            li = input('Informe a linha: ')

            if li not in alfabeto_num:
                print('Linha inválida')

            else:
                t = True

        t = False

        while t == False:

            orientacao = input('Informe a orientação [v/h]: ')
            orientacao.lower()
           
            if orientacao != 'v' and orientacao != 'h':
                print('Orientação inválida')

            else:
                t = True

        l = int(li)-1
        t = alfabeto[le]
        posicao = posicao_suporta(player_map,cubo,l,t,orientacao)

        if posicao == False:
            print(f'Não foi possivel posicionar o barco em {le}{li} {orientacao}')

################# REPRESENTAÇÃO DO MAPA (PRINT) ##################

            exibicao = [f'''  COMPUTADOR - {pais_comp}                   JOGADOR - {player_pais}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
            for i in range(9):

                exibicao.append(f'  {i+1} {aparencia_comp[i][0]}{aparencia_comp[i][1]}{aparencia_comp[i][2]}{aparencia_comp[i][3]}{aparencia_comp[i][4]}{aparencia_comp[i][5]}{aparencia_comp[i][6]}{aparencia_comp[i][7]}{aparencia_comp[i][8]}{aparencia_comp[i][9]} {i+1}    {i+1} {aparencia_player[i][0]}{aparencia_player[i][1]}{aparencia_player[i][2]}{aparencia_player[i][3]}{aparencia_player[i][4]}{aparencia_player[i][5]}{aparencia_player[i][6]}{aparencia_player[i][7]}{aparencia_player[i][8]}{aparencia_player[i][9]} {i+1}')
            
            i+=1

            exibicao.append(f' 10 {aparencia_comp[i][0]}{aparencia_comp[i][1]}{aparencia_comp[i][2]}{aparencia_comp[i][3]}{aparencia_comp[i][4]}{aparencia_comp[i][5]}{aparencia_comp[i][6]}{aparencia_comp[i][7]}{aparencia_comp[i][8]}{aparencia_comp[i][9]} 10  10 {aparencia_player[i][0]}{aparencia_player[i][1]}{aparencia_player[i][2]}{aparencia_player[i][3]}{aparencia_player[i][4]}{aparencia_player[i][5]}{aparencia_player[i][6]}{aparencia_player[i][7]}{aparencia_player[i][8]}{aparencia_player[i][9]} 10')
            exibicao.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
            
            for x in exibicao:
                print(x)

#####################################################################

            print(f'Alocar: {colocar[0]} ({cubo} blocos)')

            if len(colocar) > 0:
                perto = colocar[0]

                for i in range(1,len(colocar)):
                    perto += ', ' + colocar[i]

                print(f'Próximos: {perto}')

    print('Navio alocado!')

    for i in range(cubo):

        if orientacao == 'v':
            player_map[l+i][t] = 'N'
            aparencia_player[l+i][t] = f'\u001b[32m{espaco}\u001b[0m'

        elif orientacao == 'h':
            player_map[l][t+i] = 'N'
            aparencia_player[l][t+i] = f'\u001b[32m{espaco}\u001b[0m'

############ INICIALIZAÇÃO DO TEMPO ####################

print('Iniciando batalha naval!')

t_lista = [5,4,3,2,1]

for t in t_lista:
    print(t)
    time.sleep(1)

comp_win = False
player_win = False

##### REINICIAÇÃO DO JOGO #####

reinicio = 's'

while reinicio == 's':
    while player_win == False and comp_win == False:
        exibicao = [f'''  COMPUTADOR - {pais_comp}                   JOGADOR - {player_pais}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
        
        for i in range(9):
            exibicao.append(f'  {i+1} {aparencia_comp[i][0]}{aparencia_comp[i][1]}{aparencia_comp[i][2]}{aparencia_comp[i][3]}{aparencia_comp[i][4]}{aparencia_comp[i][5]}{aparencia_comp[i][6]}{aparencia_comp[i][7]}{aparencia_comp[i][8]}{aparencia_comp[i][9]} {i+1}    {i+1} {aparencia_player[i][0]}{aparencia_player[i][1]}{aparencia_player[i][2]}{aparencia_player[i][3]}{aparencia_player[i][4]}{aparencia_player[i][5]}{aparencia_player[i][6]}{aparencia_player[i][7]}{aparencia_player[i][8]}{aparencia_player[i][9]} {i+1}')
        
        i+=1
        
        exibicao.append(f' 10 {aparencia_comp[i][0]}{aparencia_comp[i][1]}{aparencia_comp[i][2]}{aparencia_comp[i][3]}{aparencia_comp[i][4]}{aparencia_comp[i][5]}{aparencia_comp[i][6]}{aparencia_comp[i][7]}{aparencia_comp[i][8]}{aparencia_comp[i][9]} 10  10 {aparencia_player[i][0]}{aparencia_player[i][1]}{aparencia_player[i][2]}{aparencia_player[i][3]}{aparencia_player[i][4]}{aparencia_player[i][5]}{aparencia_player[i][6]}{aparencia_player[i][7]}{aparencia_player[i][8]}{aparencia_player[i][9]} 10')
        exibicao.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
        
        for x in exibicao:
            print(x)

        print('Cordenadas do seu disparo')

####### PLAYER BOMB #######

        posicao = False

        while posicao == False:
            t = False

            while t == False:
                le = input('Informe a letra: ')
                le = le.upper()

                if le not in alfabeto:
                    print('Letra inválida')

                else:
                    t = True
            
            t = False

            while t == False:
                li = input('Informe a linha: ')

                if li not in alfabeto_num:
                    print('Linha inválida')

                else:
                    t = True

            l = int(li)-1
            t = alfabeto[le]

            if mapa_comp[l][t] != 'B' and mapa_comp[l][t] != 'A':
                posicao = True

            else:
                print(f'Posição {le}{li} já Bombardeada!')

        if mapa_comp[l][t] == 'N':
            mapa_comp[l][t] = 'B'
            aparencia_comp[l][t] = f'\u001b[31m{espaco}\u001b[0m'
        
        else:
            mapa_comp[l][t] = 'A'
            aparencia_comp[l][t] = f'\u001b[34m{espaco}\u001b[0m'

        le1 = le
        li1 = li