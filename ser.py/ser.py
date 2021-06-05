#Importação das bibliotecas
import pygame
from random import randrange
from random import randint

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
amarelo = (255,255,0)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura=320
altura=280
tamanho = 10
placar = 40
#fps, tamanho da tela,  nome do jogo, e fonte de texto
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Ser.pynte")
font = pygame.font.SysFont(None, 15)
corcobra = preto
corfundo = branco



#função de texto
def texto(msg, cor,tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x,y])
def perguntas(n):
    if n == 1:
        print("oi")
        texto("1- Python é uma linguagem: ", vermelho, 25, 55, 30)
        pygame.draw.rect(fundo, preto, [45, 120, 135 ,27])
        texto("Interpretada", branco, 30, 50 ,125)
        pygame.draw.rect(fundo, preto, [190, 120, 120, 27])
        texto("Compilada", branco, 30, 195 ,125)
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #          if event.key == pygame.K_1:
        #             break
    # if n == 2:
    if n == 3:
        corcobra = amarelo
    # if n == 4:
    # if n == 5:
    # if n == 6:
    # if n == 7:
    # if n == 8:
    # if n == 9:


#função da cobra
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, corcobra, [XY[0], XY[1], tamanho, tamanho])

#função da maça
def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])
#função do jogo
def jogo():
    sair = True
    fimdejogo = False
    pos_x=randrange(0,largura-tamanho,10)
    pos_y=randrange(0,altura-tamanho - placar,10)
    maca_x=randrange(0,largura-tamanho,10)
    maca_y=randrange(0,altura-tamanho - placar,10)
    velocidade_x=0
    velocidade_y=0
    CobraXY = []
    CobraComp = 1
    pontos = 0
    pergunta = 1
    despausar = True
    telamorte = True
    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x=randrange(0,largura-tamanho,10)
                        pos_y=randrange(0,altura-tamanho - placar,10)
                        maca_x=randrange(0,largura-tamanho,10)
                        maca_y=randrange(0,altura-tamanho - placar,10)
                        velocidade_x=0
                        velocidade_y=0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                        pergunta = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                    if pontos == 3:
                        if event.type == pygame.K_1:
                            sair = False

                #Mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        sair = True
                        fimdejogo = False
                        pos_x=randrange(0,largura-tamanho,10)
                        pos_y=randrange(0,altura-tamanho - placar,10)
                        maca_x=randrange(0,largura-tamanho,10)
                        maca_y=randrange(0,altura-tamanho - placar,10)
                        velocidade_x=0
                        velocidade_y=0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                        pergunta = 0
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        sair = False
                        fimdejogo = False
            if telamorte:
                fundo.fill(corfundo)
                texto("Fim de jogo", vermelho, 50, 65, 30)
                texto("Pontuação Final: " +str(pontos), preto, 30, 70, 80)
                pygame.draw.rect(fundo, preto, [45, 120, 135 ,27])
                texto("Continuar(C)", branco, 30, 50 ,125)
                pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
                texto("Sair(S))", branco, 30, 195 ,125)
                pygame.display.update()
        #movimentação cobra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=-tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y=0
                    velocidade_x=tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=-tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x=0
                    velocidade_y=tamanho
        #questão estetica do código para o fim de jogo
        if sair:
            fundo.fill(corfundo)
            pos_x+=velocidade_x
            pos_y+=velocidade_y

            
            #posicionamento da maça
            if pos_x == maca_x and pos_y == maca_y:
                maca_x=randrange(0,largura-tamanho,10)
                maca_y=randrange(0,altura-tamanho - 40,10)
                CobraComp += 1
                pontos += 1
                if pontos == 3:
                    fimdejogo = True
                    sair = True
                    telamorte = False
                # if pontos % 3 == 0:
                    # pergunta += 1
                    # despausar = False
                    # perguntas(pergunta)
                    # pygame.display.update()
                # else:
                    # despausar = True
                
            if despausar:
                #Regras de parede 
                if pos_x + tamanho > largura:
                    pos_x = 0
                if pos_x < 0:
                    pos_x=largura-tamanho
                if pos_y + tamanho> altura - placar:
                    pos_y = 0
                if pos_y < 0:
                    pos_y= altura-tamanho - placar
                    
                CobraInicio = []
                CobraInicio.append(pos_x)
                CobraInicio.append(pos_y)
                CobraXY.append(CobraInicio)
                if len(CobraXY) > CobraComp:
                    del CobraXY[0]
                #fim de jogo, colisão da cobra com sí própria
                if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                    fimdejogo = True
                    telamorte = True

                pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])
                texto("Pontuação: "+str(pontos), branco, 20, 10, altura - 30)
                cobra(CobraXY)
                maca(maca_x,maca_y)
                pygame.display.update()
                relogio.tick(20)

jogo()
pygame.quit()