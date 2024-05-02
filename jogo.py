############
### JOGO ###
############

#**********************************#  JOGO  #*********************************#

### define o pais do computador ###
mapa = cria_mapa(10)
paises = ['Brasil','França','Austrália','Rússia','Japão']
p = ['1','2','3','4','5']
pais_pc = random.choice(paises)
navios_pc = []
for navio in PAISES[pais_pc]:
    for i in range(PAISES[pais_pc][navio]):
        navios_pc.append(CONFIGURACAO[navio])
mapa_pc = aloca_navios(mapa,navios_pc)


### printa as mensagens iniciais ###
welcome = ''' ===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= '''

aviso = f'Iniciando o jogo!\n\nComputador está alocando os navios de guerra do país {pais_pc}...\nComputador já está em posição de batalha!'

config = '''
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

print(f'{welcome}\n\n{aviso}\n{config}')

### define o pais do jogador ###
jogador = input('Qual o número da nação da sua frota? ')
while jogador not in p:
    print('Opção inválida')
    jogador = input('Qual o número da nação da sua frota? ')
print(f'Você escolheu a nação {paises[int(jogador)-1]}\nAgora é sua vez de alocar seus navios de guerra!')
pais_jogador = paises[int(jogador)-1]


x = '▓▓▓'

### cria o mapa ###
visual_pc = cria_visual(10)
visual_jogador = cria_visual(10)
mapa_jogador = cria_mapa(10)

alocar = []
for navio in PAISES[pais_jogador]:
    for i in range(PAISES[pais_jogador][navio]):
        alocar.append(navio)

### loop de alocar navios ###

for i in range(len(alocar)):

    ### print do mapa ###
    display = [f'''  COMPUTADOR - {pais_pc}                   JOGADOR - {pais_jogador}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
    for i in range(9):
        display.append(f'  {i+1} {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} {i+1}    {i+1} {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} {i+1}')
    i+=1
    display.append(f' 10 {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} 10  10 {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} 10')
    display.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
    for a in display:
        print(a)
    #####################

    blocos = CONFIGURACAO[alocar[0]]
    print(f'Alocar: {alocar[0]} ({blocos} blocos)')
    del alocar[0]
    if len(alocar) > 0:
        prox = alocar[0]
        for i in range(1,len(alocar)):
            prox += ', ' + alocar[i]
        print(f'Próximos: {prox}')

    posicao = False

    while posicao == False:
        c = False

        while c == False:
            letra = input('Informe a letra: ')
            letra = letra.upper()
            if letra not in ori:
                print('Letra inválida')
            else:
                c = True
        
        c = False
        while c == False:
            linha = input('Informe a linha: ')
            if linha not in ori_num:
                print('Linha inválida')
            else:
                c = True

        c = False
        while c == False:
            orientacao = input('Informe a orientação [v/h]: ')
            orientacao.lower()
            if orientacao != 'v' and orientacao != 'h':
                print('Orientação inválida')
            else:
                c = True

        l = int(linha)-1
        c = ori[letra]
        posicao = posicao_suporta(mapa_jogador,blocos,l,c,orientacao)
        if posicao == False:
            print(f'Não foi possivel alocar o navio em {letra}{linha} {orientacao}')
            ### print do mapa ###
            display = [f'''  COMPUTADOR - {pais_pc}                   JOGADOR - {pais_jogador}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
            for i in range(9):
                display.append(f'  {i+1} {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} {i+1}    {i+1} {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} {i+1}')
            i+=1
            display.append(f' 10 {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} 10  10 {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} 10')
            display.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
            for a in display:
                print(a)
            #####################
            print(f'Alocar: {alocar[0]} ({blocos} blocos)')
            if len(alocar) > 0:
                prox = alocar[0]
                for i in range(1,len(alocar)):
                    prox += ', ' + alocar[i]
                print(f'Próximos: {prox}')

    print('Navio alocado!')

    for i in range(blocos):
        if orientacao == 'v':
            mapa_jogador[l+i][c] = 'N'
            visual_jogador[l+i][c] = f'\u001b[32m{x}\u001b[0m'
        elif orientacao == 'h':
            mapa_jogador[l][c+i] = 'N'
            visual_jogador[l][c+i] = f'\u001b[32m{x}\u001b[0m'

### start print ###
print('Iniciando batalha naval!')
tempos = [5,4,3,2,1]
for tempo in tempos:
    print(tempo)
    time.sleep(1)


vitoria_pc = False
vitoria_jogador = False

### loop do jogo ###
restart = 's'
while restart == 's':
    while vitoria_jogador == False and vitoria_pc == False:
        ### print do mapa ###
        display = [f'''  COMPUTADOR - {pais_pc}                   JOGADOR - {pais_jogador}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
        for i in range(9):
            display.append(f'  {i+1} {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} {i+1}    {i+1} {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} {i+1}')
        i+=1
        display.append(f' 10 {visual_pc[i][0]}{visual_pc[i][1]}{visual_pc[i][2]}{visual_pc[i][3]}{visual_pc[i][4]}{visual_pc[i][5]}{visual_pc[i][6]}{visual_pc[i][7]}{visual_pc[i][8]}{visual_pc[i][9]} 10  10 {visual_jogador[i][0]}{visual_jogador[i][1]}{visual_jogador[i][2]}{visual_jogador[i][3]}{visual_jogador[i][4]}{visual_jogador[i][5]}{visual_jogador[i][6]}{visual_jogador[i][7]}{visual_jogador[i][8]}{visual_jogador[i][9]} 10')
        display.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
        for a in display:
            print(a)
        #####################
        print('Cordenadas do seu disparo')

        ### bomba do jogador ###
        posi = False
        while posi == False:
            c = False
            while c == False:
                letra = input('Informe a letra: ')
                letra = letra.upper()
                if letra not in ori:
                    print('Letra inválida')
                else:
                    c = True
            
            c = False
            while c == False:
                linha = input('Informe a linha: ')
                if linha not in ori_num:
                    print('Linha inválida')
                else:
                    c = True

            l = int(linha)-1
            c = ori[letra]
            if mapa_pc[l][c] != 'B' and mapa_pc[l][c] != 'A':
                posi = True
            else:
                print(f'Posição {letra}{linha} já Bombardeada!')
        if mapa_pc[l][c] == 'N':
            mapa_pc[l][c] = 'B'
            visual_pc[l][c] = f'\u001b[31m{x}\u001b[0m'
        else:
            mapa_pc[l][c] = 'A'
            visual_pc[l][c] = f'\u001b[34m{x}\u001b[0m'
        letra1 = letra
        linha1 = linha

        ### bomba do computador ###
        pos = False
        while pos == False:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if mapa_jogador[linha][coluna] == ' ' or mapa_jogador[linha][coluna] == 'N':
                pos = True
                if mapa_jogador[linha][coluna] == 'N':
                    mapa_jogador[linha][coluna] = 'B'
                    visual_jogador[linha][coluna] = f'\u001b[31m{x}\u001b[0m'
                elif mapa_jogador[linha][coluna] == ' ':
                    mapa_jogador[linha][coluna] = 'A'
                    visual_jogador[linha][coluna] = f'\u001b[34m{x}\u001b[0m'
            


        ori1 = {}
        for key,valor in ori.items():
            ori1[valor+1] = key

        ### prints ###
        if mapa_jogador[linha][coluna] == 'A':
            jog = 'Água!'
        elif mapa_jogador[linha][coluna] == 'B':
            jog = 'BOOOOMMMMM!'
        
        if mapa_pc[l][c] == 'A':
            pc = 'Água!'
        elif mapa_pc[l][c] == 'B':
            pc = 'BOOOOMMMMM!'


        print(f'Jogador ---->>>> {letra1}{linha1}    {pc}\nComputador ---->>>> {ori1[coluna+1]}{linha+1}    {jog}')

        vitoria_jogador = foi_derrotado(mapa_pc)
        vitoria_pc = foi_derrotado(mapa_jogador)

        if vitoria_jogador == True:
            print('Você venceu!\nTemos um novo xerife nos mares!')
        elif vitoria_pc == True:
            print('Você perdeu!\nO computador ainda é o senhor dos mares')

    restart = (input('Jogar novamente? [s/n] ')).lower()
    vitoria_pc = False
    vitoria_jogador = False
print('\n\nAté a proxima!')