import turtle as t
import functools
import random
import math
import time

LARGURA_JANELA = 1024
ALTURA_JANELA = 600
DEFAULT_TURTLE_SIZE = 65
DEFAULT_TURTLE_SCALE = 2
RAIO_JOGADOR = DEFAULT_TURTLE_SIZE / DEFAULT_TURTLE_SCALE
RAIO_BOLA = DEFAULT_TURTLE_SIZE / 8
PIXEIS_MOVIMENTO = 45
LADO_MAIOR_AREA = ALTURA_JANELA / 3
LADO_MENOR_AREA = 50
RAIO_MEIO_CAMPO = LADO_MAIOR_AREA / 4
START_POS_BALIZAS = ALTURA_JANELA / 4
BOLA_START_POS = (0, 0)
VELOCIDADE_BOLA = 6

# Funções responsáveis pelo movimento dos jogadores no ambiente. 
# O número de unidades que o jogador se pode movimentar é definida pela constante 
# PIXEIS_MOVIMENTO. As funções recebem um dicionário que contém o estado 
# do jogo e o jogador que se está a movimentar. 

g = t.Turtle()
g.ht()

def escrever_golo(cor):
    if cor == "azul": 
        g.pencolor("blue")
        player_marcador = "Player B"
    elif cor == "vermelho": 
        g.pencolor("red")
        player_marcador = "Player A"
    g.up()
    g.ht()
    g.goto(0,-230)
    g.write("G O L O O O",align="center", font=('Germania One',65,"bold"))
    g.goto(0,-250)
    g.write(f"{player_marcador} - {tempo//60}' {tempo-(60*(tempo//60)):02d}''",align="center", font=('Germania One',15,"bold"))

def jogador_cima(estado_jogo, jogador):
    if(estado_jogo[jogador].ycor() < 270 ):
        estado_jogo[jogador].setheading(90)
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
    pass

def jogador_baixo(estado_jogo, jogador):
    if(estado_jogo[jogador].ycor() > -270 ):
        estado_jogo[jogador].setheading(270)
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
    pass
    
def jogador_direita(estado_jogo, jogador):
    if(estado_jogo[jogador].xcor() < 470 ):
        estado_jogo[jogador].setheading(0)
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
    pass

def jogador_esquerda(estado_jogo, jogador):
    if(estado_jogo[jogador].xcor() > -470 ):
        estado_jogo[jogador].setheading(180)
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
    pass


def temporizador(timer_turtle,iniciamento):
    inicio = iniciamento
    timer = timer_turtle
    timer.color("white")
    timer.up()
    timer.goto(-500,290)
    timer.down()
    timer.begin_fill()
    for i in range(2):
        timer.fd(74)
        timer.rt(90)
        timer.fd(34)
        timer.rt(90)
    timer.end_fill()
    timer.pencolor("black")
    timer.up()
    timer.goto(-460,256)
    global tempo
    tempo = int(time.time() - inicio)
    timer.write(f"{tempo//60}:{tempo-(60*(tempo//60)):02d}",align="center", font=("Time New Roman", 27))
    timer.ht()
    return timer


def desenha_linhas_campo():
    t.up()
    for i in range(0,8):
        t.fillcolor("forest green")
        t.goto(-512 + 128*(i),-300)
        t.begin_fill()
        t.fd(128)
        t.lt(90)
        t.fd(600)
        t.lt(90)
        t.fd(128)
        t.end_fill()
        
    t.pencolor("white")
    t.width(10)
    t.goto(0,-5)
    t.down()
    t.circle(4)
    t.up()
    t.goto(0,-100)
    t.down()
    t.circle(100)
    t.goto(0,-300)
    t.lt(90)
    t.fd(600)
    t.up()
    for i in range(2):
        if i == 0:
            t.goto(-512,-110)
            t.rt(90)
        else:
            t.goto(458,-110)
            t.lt(90)
        t.down()
        for x in range(2):
            t.fd(50)
            t.lt(90)
            t.fd(220)
            if x == 0: t.lt(90)
        t.up()

    for i in range(2):
        if i == 0: t.goto(-512,-200)
        else: 
            t.goto(512,200)
            t.right(90)
        t.down()
        t.left(90)
        t.fd(200)
        t.left(90)
        t.fd(400)
        t.left(90)
        t.fd(200)
        t.up()

    for i in range(2):
        t.goto(390*(-1)**i,-4)
        t.down()
        t.circle(4)
        t.up()
        t.ht()
    t.width(1)
    
    ''' Função responsável por desenhar as linhas do campo, 
    nomeadamente a linha de meio campo, o círculo central, e as balizas. '''
    pass


def criar_bola():
    direcao_x = random.uniform(-1,1)
    direcao_y = random.uniform(-1,1)
    while (direcao_x**2 + direcao_y**2 <= 1):
        direcao_x = direcao_x*1.1
        direcao_y = direcao_y*1.1
    tbola = t.Turtle()
    tbola.up()
    tbola.setpos(BOLA_START_POS)
    tbola.down()
    tbola.color("black")
    tbola.turtlesize(1.5)
    tbola.shape("circle")
    tbola.up()

    return({"bola": tbola,"direcao_x": direcao_x, "direcao_y":direcao_y, "posicao_anterior" :None })
   
    '''
    Função responsável pela criação da bola. 
    Deverá considerar que esta tem uma forma redonda, é de cor preta, 
    começa na posição BOLA_START_POS com uma direção aleatória. 
    Deverá ter em conta que a velocidade da bola deverá ser superior à dos jogadores. 
    A função deverá devolver um dicionário contendo 4 elementos: o objeto bola, 
    a sua direção no eixo dos xx, a sua direção no eixo dos yy, 
    e um elemento inicialmente a None que corresponde à posição anterior da mesma.
    '''
    pass


def cria_jogador(x_pos_inicial, y_pos_inicial, cor):
    jogador = t.Turtle()
    jogador.up()
    jogador.setpos(x_pos_inicial, y_pos_inicial)
    jogador.down()
    jogador.color(cor)
    jogador.turtlesize(3)
    jogador.shape("circle")
    jogador.up()
    
    return(jogador)

    ''' Função responsável por criar e devolver o objeto que corresponde a um jogador (um objecto Turtle). 
    A função recebe 3 argumentos que correspondem às coordenadas da posição inicial 
    em xx e yy, e a cor do jogador. A forma dos jogadores deverá ser um círculo, 
    cujo seu tamanho deverá ser definido através da função shapesize
    do módulo \texttt{turtle}, usando os seguintes parâmetros: 
    stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE. '''
    pass


def init_state():
    estado_jogo = {}
    estado_jogo['bola'] = None
    estado_jogo['jogador_vermelho'] = None
    estado_jogo['jogador_azul'] = None
    estado_jogo['var'] = {
        'bola' : [],
        'jogador_vermelho' : [],
        'jogador_azul' : [],
    }
    estado_jogo['pontuacao_jogador_vermelho'] = 0
    estado_jogo['pontuacao_jogador_azul'] = 0
    return estado_jogo

def cria_janela():
    #create a window and declare a variable called window and call the screen()
    window=t.Screen()
    window.title("Liga dos Últimos")
    window.bgcolor("green")
    window.setup(width = LARGURA_JANELA,height = ALTURA_JANELA)
    window.tracer(0)
    return window

def cria_quadro_resultados():
    #Code for creating pen for scorecard update
    quadro=t.Turtle()
    quadro.speed(0)
    quadro.color("Blue")
    quadro.penup()
    quadro.hideturtle()
    quadro.pencolor("yellow")
    quadro.fillcolor("#2e313f")
    quadro.goto(-420,290)
    quadro.begin_fill()
    for i in range(2):
        quadro.fd(360)
        quadro.right(90)
        quadro.fd(35)
        quadro.right(90)
    quadro.end_fill()
    quadro.right(90)
    quadro.fillcolor("red")
    quadro.begin_fill()
    for i in range(2):
        quadro.fd(35)
        quadro.rt(90)
        quadro.fd(5)
        quadro.rt(90)
    quadro.end_fill()
    quadro.goto(-60,290)
    quadro.fillcolor("blue")
    quadro.begin_fill()
    for i in range(2):
        quadro.fd(35)
        quadro.rt(90)
        quadro.fd(5)
        quadro.rt(90)
    quadro.end_fill()
    quadro.goto(-240,260)
    quadro.write("Player A | 0 - 0 | Player B", align="center", font=('Monaco',20,"normal"))
    return quadro


def terminar_jogo(estado_jogo):
    with open("histórico_resultados.csv", "a+") as ficheiro:
        ficheiro.seek(0)
        if not ficheiro.read():
            ficheiro.write("NJogo,JogadorVermelho,JogadorAzul")
            ultima_linha = "0"
        else:
            ficheiro.seek(2)
            ultima_linha = ficheiro.readlines()[-1]
            ultima_linha = ultima_linha.split(',')
        ficheiro.write(f"\n{str(int(ultima_linha[0])+1)},{estado_jogo['pontuacao_jogador_vermelho']},{estado_jogo['pontuacao_jogador_azul']}")
        
    '''
     Função responsável por terminar o jogo. Nesta função, deverá atualizar o ficheiro 
     ''historico_resultados.csv'' com o número total de jogos até ao momento, 
     e o resultado final do jogo. Caso o ficheiro não exista, 
     ele deverá ser criado com o seguinte cabeçalho: 
     NJogo,JogadorVermelho,JogadorAzul.
    '''
    print("Adeus")
    estado_jogo['janela'].bye()
    

def setup(estado_jogo, jogar):
    janela = cria_janela()
    #Assign keys to play
    janela.listen()
    desenha_linhas_campo()
    if jogar:
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_vermelho') ,'w')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_vermelho') ,'s')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_vermelho') ,'a')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_vermelho') ,'d')
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_azul') ,'Up')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_azul') ,'Down')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_azul') ,'Left')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_azul') ,'Right')
        janela.onkeypress(functools.partial(terminar_jogo, estado_jogo) ,'Escape')
        quadro = cria_quadro_resultados()
        estado_jogo['quadro'] = quadro
    bola = criar_bola()
    jogador_vermelho = cria_jogador(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "red")
    jogador_azul = cria_jogador(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "blue")
    estado_jogo['janela'] = janela
    estado_jogo['bola'] = bola
    estado_jogo['jogador_vermelho'] = jogador_vermelho
    estado_jogo['jogador_azul'] = jogador_azul

def update_board(estado_jogo):
    quadro = estado_jogo['quadro']
    quadro.clear()
    quadro.setheading(0)
    quadro.pencolor("yellow")
    quadro.fillcolor("#2e313f")
    quadro.goto(-420,290)
    quadro.begin_fill()
    for i in range(2):
        quadro.fd(360)
        quadro.right(90)
        quadro.fd(35)
        quadro.right(90)
    quadro.end_fill()
    quadro.right(90)
    quadro.fillcolor("red")
    quadro.begin_fill()
    for i in range(2):
        quadro.fd(35)
        quadro.rt(90)
        quadro.fd(5)
        quadro.rt(90)
    quadro.end_fill()
    quadro.goto(-60,290)
    quadro.fillcolor("blue")
    quadro.begin_fill()
    for i in range(2):
        quadro.fd(35)
        quadro.rt(90)
        quadro.fd(5)
        quadro.rt(90)
    quadro.end_fill()
    quadro.goto(-240,260)
    quadro.write("Player A | {} - {} | Player B".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']),align="center",font=('Monaco',20,"normal"))

def movimenta_bola(estado_jogo):
    bola = estado_jogo['bola'].get('bola')
    estado_jogo['bola']['posicao_anterior'] = bola.pos()
    direcao_x = estado_jogo['bola'].get('direcao_x')
    direcao_y = estado_jogo['bola'].get('direcao_y')
    bola.goto(bola.xcor()+direcao_x*VELOCIDADE_BOLA, bola.ycor()+direcao_y*VELOCIDADE_BOLA)

    
    '''
    Função responsável pelo movimento da bola que deverá ser feito tendo em conta a
    posição atual da bola e a direção em xx e yy.
    '''
    pass

def verifica_colisoes_ambiente(estado_jogo):
    tbola = estado_jogo['bola'].get('bola')
    if tbola.xcor() >= 490:
        estado_jogo['bola']['direcao_x'] = -(estado_jogo['bola'].get('direcao_x'))
    elif tbola.xcor() <= -490:
        estado_jogo['bola']['direcao_x'] = -(estado_jogo['bola'].get('direcao_x'))
    if tbola.ycor() >= 290:
        estado_jogo['bola']['direcao_y'] = -(estado_jogo['bola'].get('direcao_y'))
    elif tbola.ycor() <= -290:
        estado_jogo['bola']['direcao_y']= -(estado_jogo['bola'].get('direcao_y'))

    
    '''
    Função responsável por verificar se há colisões com os limites do ambiente, 
    atualizando a direção da bola. Não se esqueça de considerar que nas laterais, 
    fora da zona das balizas, a bola deverá inverter a direção onde atingiu o limite.
    '''
    pass


def verifica_golo_jogador_vermelho(estado_jogo):
    bola = estado_jogo['bola'].get('bola')
    x_antigo, y_antigo = estado_jogo['bola']['posicao_anterior']
    if 488  < bola.xcor() < 500 and -85 < bola.ycor() < 85   :
        g.clear()
        bola.goto(0,0)
        estado_jogo['pontuacao_jogador_vermelho'] += 1
        update_board(estado_jogo)
        direcao_x = random.uniform(-1,1)
        direcao_y = random.uniform(-1,1) 
        while (direcao_x**2 + direcao_y**2 <= 1):
            direcao_x = direcao_x*1.1
            direcao_y = direcao_y*1.1   
        estado_jogo['bola']['direcao_x'] = direcao_x
        estado_jogo['bola']['direcao_y'] = direcao_y

        with open('replay_golo_jv_{}_ja_{}.txt'.format(estado_jogo['pontuacao_jogador_vermelho'],estado_jogo['pontuacao_jogador_azul']), 'w') as f:

            ponto_virgula = ";"*(len(estado_jogo['var']['bola'])-1) + " "

            for i in range(len(estado_jogo['var']['bola'])):
                f.write('{:.2f},{:.2f}'.format(estado_jogo['var']['bola'][i][0], estado_jogo['var']['bola'][i][1]))
                f.write(ponto_virgula[i])
            f.write('\n') 
            for i in range(len(estado_jogo['var']['jogador_vermelho'])):
                f.write('{:.2f},{:.2f}'.format(estado_jogo['var']['jogador_vermelho'][i][0], estado_jogo['var']['jogador_vermelho'][i][1]))
                f.write(ponto_virgula[i])
            f.write('\n')
            for i in range(len(estado_jogo['var']['jogador_azul'])):
                f.write('{:.2f},{:.2f}'.format(estado_jogo['var']['jogador_azul'][i][0], estado_jogo['var']['jogador_azul'][i][1]))
                f.write(ponto_virgula[i])
            f.write('\n')
        escrever_golo("vermelho")
        estado_jogo['var']['bola'] = list()
        estado_jogo['var']['jogador_vermelho'] = list()
        estado_jogo['var']['jogador_azul'] = list()
        return time.time()
    return(-1)


    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    pass

def verifica_golo_jogador_azul(estado_jogo):
    bola = estado_jogo['bola'].get('bola')
    if -500 < bola.xcor() < -489 and -85 < bola.ycor() < 85:
        g.clear()
        bola.goto(0,0)
        estado_jogo['pontuacao_jogador_azul'] += 1
        update_board(estado_jogo)
        direcao_x = random.uniform(-1,1)
        direcao_y = random.uniform(-1,1)
        while (direcao_x**2 + direcao_y**2 <= 1):
            direcao_x = direcao_x*1.1
            direcao_y = direcao_y*1.1
        estado_jogo['bola']['direcao_x'] = direcao_x
        estado_jogo['bola']['direcao_y'] = direcao_y
        
        with open('replay_golo_jv_{}_ja_{}.txt'.format(estado_jogo['pontuacao_jogador_vermelho'],estado_jogo['pontuacao_jogador_azul']), 'w') as f:

            ponto_virgula = ";"*(len(estado_jogo['var']['bola'])-1) + " "

            for i in range(len(estado_jogo['var']['bola'])):
                f.write('{:.2f},{:.2f}'.format(estado_jogo['var']['bola'][i][0], estado_jogo['var']['bola'][i][1]))
                f.write(ponto_virgula[i])
            f.write('\n') 
            for i in range(len(estado_jogo['var']['jogador_vermelho'])):
                f.write('{:.2f},{:.2f}'.format(estado_jogo['var']['jogador_vermelho'][i][0], estado_jogo['var']['jogador_vermelho'][i][1]))
                f.write(ponto_virgula[i])
            f.write('\n')
            for i in range(len(estado_jogo['var']['jogador_azul'])):
                f.write('{:.2f},{:.2f}'.format(estado_jogo['var']['jogador_azul'][i][0], estado_jogo['var']['jogador_azul'][i][1]))
                f.write(ponto_virgula[i])
            f.write('\n')
        
        estado_jogo['var']['bola'] = list()
        estado_jogo['var']['jogador_vermelho'] = list()
        estado_jogo['var']['jogador_azul'] = list()
        escrever_golo("azul")
        return time.time()
    return(-1)
            


    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    pass


def verifica_golos(estado_jogo):
    return verifica_golo_jogador_vermelho(estado_jogo), verifica_golo_jogador_azul(estado_jogo)


def verifica_toque_jogador_azul(estado_jogo):
    entrou = 0
    bola = estado_jogo['bola'].get('bola')
    jogador_azul = estado_jogo['jogador_azul']
    x_antigo, y_antigo = estado_jogo['bola']['posicao_anterior']
    if(time.time() - entrou >= 0.05):
        if (((jogador_azul.xcor()-x_antigo)**2+(jogador_azul.ycor()-y_antigo)**2) <= RAIO_JOGADOR **2):
            entrou = time.time()
            angulo = jogador_azul.towards(bola.xcor(),bola.ycor())
            estado_jogo['bola']['direcao_y']= math.sin(90- angulo)
            estado_jogo['bola']['direcao_x']= math.cos(90- angulo)
            if estado_jogo['bola']['direcao_x'] >= 0:
                if estado_jogo['bola']['direcao_y'] >= 0:
                    bola.goto(x_antigo + RAIO_BOLA, y_antigo + RAIO_BOLA)
                elif(estado_jogo['bola']['direcao_y']) < 0:
                    bola.goto(x_antigo + RAIO_BOLA, y_antigo - RAIO_BOLA)

            elif estado_jogo['bola']['direcao_x'] < 0:
                if estado_jogo['bola']['direcao_y'] >= 0:
                    bola.goto(x_antigo - RAIO_BOLA, y_antigo + RAIO_BOLA)

                elif(estado_jogo['bola']['direcao_y']) < 0:
                    bola.goto(x_antigo - RAIO_BOLA, y_antigo - RAIO_BOLA)

    else:
        if (bola.distance(jogador_azul) <=  RAIO_BOLA + RAIO_JOGADOR):
            angulo = jogador_azul.towards(bola.xcor(),bola.ycor())
            estado_jogo['bola']['direcao_y']= math.sin(90- angulo)
            estado_jogo['bola']['direcao_x']= math.cos(90- angulo)
         
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    pass


def verifica_toque_jogador_vermelho(estado_jogo):
    bola = estado_jogo['bola'].get('bola')
    jogador_vermelho = estado_jogo['jogador_vermelho']
    x_antigo, y_antigo = estado_jogo['bola']['posicao_anterior']
    if (((jogador_vermelho.xcor()-x_antigo)**2+(jogador_vermelho.ycor()-y_antigo)**2) <= RAIO_JOGADOR **2):
        angulo = jogador_vermelho.towards(bola.xcor(),bola.ycor())
        estado_jogo['bola']['direcao_y']= math.sin(90- angulo)
        estado_jogo['bola']['direcao_x']= math.cos(90- angulo)
        if estado_jogo['bola']['direcao_x'] >= 0:
            if estado_jogo['bola']['direcao_y'] >= 0:
                bola.goto(x_antigo + (RAIO_JOGADOR- RAIO_BOLA), y_antigo + (RAIO_JOGADOR- RAIO_BOLA))
            elif(estado_jogo['bola']['direcao_y']) < 0:
                bola.goto(x_antigo + (RAIO_JOGADOR- RAIO_BOLA), y_antigo - (RAIO_JOGADOR- RAIO_BOLA))

        elif estado_jogo['bola']['direcao_x'] < 0:
            if estado_jogo['bola']['direcao_y'] >= 0:
                bola.goto(x_antigo - (RAIO_JOGADOR- RAIO_BOLA), y_antigo + (RAIO_JOGADOR- RAIO_BOLA))

            elif(estado_jogo['bola']['direcao_y']) < 0:
                bola.goto(x_antigo - (RAIO_JOGADOR- RAIO_BOLA), y_antigo - (RAIO_JOGADOR- RAIO_BOLA))

    else:
        if (bola.distance(jogador_vermelho) <=  RAIO_BOLA + RAIO_JOGADOR):
            angulo = jogador_vermelho.towards(bola.xcor(),bola.ycor())
            estado_jogo['bola']['direcao_y']= math.sin(90- angulo)
            estado_jogo['bola']['direcao_x']= math.cos(90- angulo)      
    
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    pass

def guarda_posicoes_para_var(estado_jogo):
    bola = estado_jogo['bola']['bola']
    jogador_azul = estado_jogo['jogador_azul']
    jogador_vermelho = estado_jogo['jogador_vermelho']
    estado_jogo['var']['bola'].append(tuple(round(valor,3)for valor in bola.pos()))
    estado_jogo['var']['jogador_vermelho'].append(tuple(round(valor,3)for valor in jogador_vermelho.pos()))
    estado_jogo['var']['jogador_azul'].append(tuple(round(valor,3)for valor in jogador_azul.pos()))


def main():
    estado_jogo = init_state()
    setup(estado_jogo, True)
    iniciamento = time.time()
    timer_turtle = t.Turtle()
    tempo_golo = -1
    while(True):
        temporizador(timer_turtle,iniciamento)
        estado_jogo['janela'].update()
        if estado_jogo['bola'] is not None:
            movimenta_bola(estado_jogo)
        verifica_colisoes_ambiente(estado_jogo)
        
        tuplo = verifica_golos(estado_jogo)
        for i in range(2):
            if tuplo[i] != -1:
                tempo_golo = tuplo[i]
        if tempo_golo!=-1 and time.time() - tempo_golo >= 1:
                tempo_golo=-1
                g.clear()
                g.ht()

        if estado_jogo['jogador_vermelho'] is not None:
            verifica_toque_jogador_azul(estado_jogo)
        if estado_jogo['jogador_azul'] is not None:
            verifica_toque_jogador_vermelho(estado_jogo)
        guarda_posicoes_para_var(estado_jogo)
        temporizador(timer_turtle,iniciamento).reset()

if __name__ == '__main__':
    main()

