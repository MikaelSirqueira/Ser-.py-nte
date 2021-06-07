# Importação das bibliotecas
from typing import final
import pygame
from random import randrange

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (1, 22, 84)
amarelo = (251, 204, 71)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura = 340
altura = 280
tamanho = 10
placar = 40
# fps, tamanho da tela,  nome do jogo, e fonte de texto
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ser.pynte")
font = pygame.font.SysFont(None, 15)
corcobra = amarelo
corfundo = azul
telafinal = False
#area de atribuição das respostas certas e erradas (em ordem 1,2,3,4,5,6,7,8,9)
escolha = [[True, False], [False, False, True, False], [False, False, False, True], [True, False, False, False],
           [False, False, True, False], [False, False, True], [False, True, False], [False, False, True],
           [False, False, False, True]]

# função de texto
def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])


def perguntas(n):
    if n == 1:
        fundo.fill(corfundo)
        texto("1- Python é uma linguagem: ", vermelho, 25, 5, 30)
        pygame.draw.rect(fundo, preto, [20, 80, 200, 27])
        texto("a)Interpretada", branco, 22, 25, 85)
        pygame.draw.rect(fundo, preto, [20, 120, 200, 27])
        texto("b)Compilada", branco, 22, 25, 125)
        pygame.display.update()
    if n == 2:
        fundo.fill(corfundo)
        texto("2-A tecla # no python é utilizada para: ", vermelho, 25, 5, 30)
        pygame.draw.rect(fundo, preto, [20, 80, 270, 27])
        texto("a)jogar um jogo da velha contra o pc", branco, 22, 25, 85)
        pygame.draw.rect(fundo, preto, [20, 120, 270, 27])
        texto("b)multiplicar duas variáveis",  branco, 22, 25, 125)
        pygame.draw.rect(fundo, preto, [20, 160, 270, 27])
        texto("c)adicionar um comentário", branco, 22, 25, 165)
        pygame.draw.rect(fundo, preto, [20, 200, 270, 27])
        texto("d)comando para inserir um valor", branco, 22, 25, 205)
        pygame.display.update()
    if n == 3:
        fundo.fill(corfundo)
        texto("3- Qual o comando para criar uma ", vermelho, 25, 5, 20)
        texto("função no python: ", vermelho, 25, 10, 45)
        pygame.draw.rect(fundo, preto, [20, 80, 270, 27])
        texto("a)function", branco, 22, 25, 85)
        pygame.draw.rect(fundo, preto, [20, 120, 270, 27])
        texto("b)void", branco, 22, 25, 125)
        pygame.draw.rect(fundo, preto, [20, 160, 270, 27])
        texto("c)echo", branco, 22, 25, 165)
        pygame.draw.rect(fundo, preto, [20, 200, 270, 27])
        texto("d)def", branco, 22, 25, 205)
        pygame.display.update()
    if n == 4:
        fundo.fill(corfundo)
        texto("4 - O comando print('5'+'3') em", vermelho, 25, 5, 20)
        texto("Python resulta em: ", vermelho, 25, 10, 45)
        pygame.draw.rect(fundo, preto, [20, 80, 270, 27])
        texto("a)53", branco, 22, 25, 85)
        pygame.draw.rect(fundo, preto, [20, 120, 270, 27])
        texto("b)2", branco, 22, 25, 125)
        pygame.draw.rect(fundo, preto, [20, 160, 270, 27])
        texto("c)8", branco, 22, 25, 165)
        pygame.draw.rect(fundo, preto, [20, 200, 270, 27])
        texto("d)nenhuma das opções", branco, 22, 25, 205)
        pygame.display.update()
    if n == 5:
        fundo.fill(corfundo)
        texto("5- Qual operador lógico para verificar", vermelho, 25, 5, 20)
        texto("se dois valores são diferentes:", vermelho, 25, 10, 45)
        pygame.draw.rect(fundo, preto, [20, 80, 270, 27])
        texto("a) >=", branco, 22, 25, 85)
        pygame.draw.rect(fundo, preto, [20, 120, 270, 27])
        texto("b) ==", branco, 22, 25, 125)
        pygame.draw.rect(fundo, preto, [20, 160, 270, 27])
        texto("c) !=", branco, 22, 25, 165)
        pygame.draw.rect(fundo, preto, [20, 200, 270, 27])
        texto("d) ≠", branco, 22, 25, 205)
        pygame.display.update()
    if n == 6:
        fundo.fill(corfundo)
        texto("6- Para o que serve a indentação:", vermelho, 25, 5, 30)
        pygame.draw.rect(fundo, preto, [20, 80, 290, 27])
        texto("a)para o código ficar mais bonito", branco, 22, 25, 85)
        pygame.draw.rect(fundo, preto, [20, 120, 290, 27])
        texto("b)para não parecer uma redação", branco, 22, 25, 125)
        pygame.draw.rect(fundo, preto, [20, 160, 290, 52])
        texto("c)para ressaltar ou definir a estrutura", branco, 22, 25, 165)
        texto("do algoritmo", branco, 22, 25, 187)
        pygame.display.update()
    if n == 7:
        fundo.fill(corfundo)
        texto("7-Por que a variável (trabalho de conclusão ", vermelho, 23, 5, 20)
        texto("de curso) não será reconhecida?", vermelho, 23, 10, 45)
        pygame.draw.rect(fundo, preto, [20, 80, 290, 52])
        texto("a)por que estamos apenas no primeiro", branco, 22, 25, 85)
        texto("semestre", branco, 22, 25, 107)
        pygame.draw.rect(fundo, preto, [20, 140, 290, 52])
        texto("b)por que variáveis não podem ter ", branco, 22, 25, 145)
        texto("espaço nem acento", branco, 22, 25, 167)
        pygame.draw.rect(fundo, preto, [20, 200, 290, 52])
        texto("c)pois uma variável não pode ter mais", branco, 22, 25, 205)
        texto("de cinco letras", branco, 22, 25, 227)
        pygame.display.update()
    if n == 8:
        fundo.fill(corfundo)
        texto("8- O que define a quebra de linha", vermelho, 25, 5, 35)
        texto("no Python:", vermelho, 25, 15, 60)
        pygame.draw.rect(fundo, preto, [20, 80, 270, 27])
        texto("a)ponto e virgula", branco, 22, 25, 85)
        pygame.draw.rect(fundo, preto, [20, 120, 270, 27])
        texto("b)indentação", branco, 22, 25, 125)
        pygame.draw.rect(fundo, preto, [20, 160, 270, 27])
        texto("c) \ n", branco, 22, 25, 165)
        pygame.display.update()
    if n == 9:
        fundo.fill(corfundo)
        texto("9- O que este código irá retornar?", vermelho, 25, 5, 15)
        texto("a=0", vermelho, 17, 110, 32)
        texto("while a>=8:", vermelho, 17, 110, 42)
        texto("if a %2 == 0:", vermelho, 17, 120, 52)
        texto("print(a)", vermelho, 17, 126, 62)
        texto("a +=1", vermelho, 17, 120, 72)
        pygame.draw.rect(fundo, preto, [20, 90, 270, 27])
        texto("a)8", branco, 22, 25, 95)
        pygame.draw.rect(fundo, preto, [20, 130, 270, 27])
        texto("b)todos os numeros até 8", branco, 22, 25, 135)
        pygame.draw.rect(fundo, preto, [20, 170, 270, 27])
        texto("c)todos os numeros impares ate 8", branco, 22, 25, 175)
        pygame.draw.rect(fundo, preto, [20, 210, 270, 27])
        texto("d)todos os numeros pares ate 8", branco, 22, 25, 215)
        pygame.display.update()


# função da cobra
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, corcobra, [XY[0], XY[1], tamanho, tamanho])


# função da maça
def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])


# função do jogo
def jogo():
    sair = True
    fimdejogo = False
    pos_x = randrange(0, largura - tamanho, 10)
    pos_y = randrange(0, altura - tamanho - placar, 10)
    maca_x = randrange(0, largura - tamanho, 10)
    maca_y = randrange(0, altura - tamanho - placar, 10)
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    CobraComp = 1
    pontos = 0
    pergunta = 0
    despausar = True
    telamorte = False
    telafinal = False
    finale = True
    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                # Mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if telamorte:
                        if x > 45 and x < 180 and y > 120  and y < 147:
                            sair = True
                            fimdejogo = False
                            pos_x = randrange(0, largura - tamanho, 10)
                            pos_y = randrange(0, altura - tamanho - placar, 10)
                            maca_x = randrange(0, largura - tamanho, 10)
                            maca_y = randrange(0, altura - tamanho - placar, 10)
                            velocidade_x = 0
                            velocidade_y = 0
                            CobraXY = []
                            CobraComp = 1
                            pontos = 0
                            pergunta = 0
                        elif x > 190 and y > 120 and x < 265 and y < 147:
                            sair = False
                            fimdejogo = False
                    if not telamorte: #vê se a resposta do jogador está correta, se estiver correta continua o jogo.
                        if pergunta == 1:
                            if x > 20 and x < 200  and y > 80 and y < 107 and escolha[0][0]: #1-a
                                sair = True
                                fimdejogo = False
                            elif x > 20 and x < 200 and y > 120  and y < 147 and not escolha[0][1]: #1-b
                                sair = False
                                fimdejogo = False

                        if pergunta == 2:
                            if x > 20 and x < 270  and y > 80 and y < 107 and not escolha[1][0]: #2-a
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 120  and y < 147 and not escolha[1][1]: #2-b
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 160  and y < 187 and escolha[1][2]: #2-c
                                sair = True
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 200  and y < 227 and not escolha[1][3]: #2-d
                                sair = False
                                fimdejogo = False

                        if pergunta == 3:
                            if x > 20 and x < 270  and y > 80 and y < 107 and not escolha[2][0]: #3-a
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 120  and y < 147 and not escolha[2][1]: #3-b
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 160  and y < 187 and not escolha[2][2]: #3-c
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 200  and y < 227 and escolha[2][3]: #3-d
                                sair = True
                                fimdejogo = False

                        if pergunta == 4:
                            if x > 20 and x < 270  and y > 80 and y < 107 and escolha[3][0]: #4-a
                                sair = True
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 120  and y < 147 and not escolha[3][1]: #4-b
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 160  and y < 187 and not escolha[3][2]: #4-c
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 200  and y < 227 and not escolha[3][3]: #4-d
                                sair = False
                                fimdejogo = False

                        if pergunta == 5:
                            if x > 20 and x < 270  and y > 80 and y < 107 and not escolha[4][0]: #5-a
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 120  and y < 147 and not escolha[4][1]: #5-b
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 160  and y < 187 and escolha[4][2]: #5-c
                                sair = True
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 200  and y < 227 and not escolha[4][3]: #5-d
                                sair = False
                                fimdejogo = False

                        if pergunta == 6:
                            if x > 20 and x < 290  and y > 80 and y < 107 and not escolha[5][0]: #6-a
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 290 and y > 120  and y < 147 and not escolha[5][1]: #6-b
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 290 and y > 160  and y < 212 and escolha[5][2]: #6-c
                                sair = True
                                fimdejogo = False

                        if pergunta == 7:
                            if x > 20 and x < 290  and y > 80 and y < 130 and not escolha[6][0]: #7-a
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 290 and y > 140  and y < 192 and escolha[6][1]: #7-b
                                sair = True
                                fimdejogo = False
                            elif x > 20 and x < 290 and y > 200  and y < 252 and not escolha[6][2]: #7-c
                                sair = False
                                fimdejogo = False

                        if pergunta == 8:
                            if x > 20 and x < 270  and y > 80 and y < 107 and not escolha[7][0]: #8-a
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 120  and y < 147 and not escolha[7][1]: #8-b
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 160  and y < 187 and escolha[7][2]: #8-c
                                sair = True
                                fimdejogo = False

                        if pergunta == 9:
                            if x > 20 and x < 270  and y > 90 and y < 117 and not escolha[8][0]: #9-a
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 130  and y < 157 and not escolha[8][1]: #9-b
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 170  and y < 197 and not escolha[8][2]: #9-c
                                sair = False
                                fimdejogo = False
                            elif x > 20 and x < 270 and y > 210  and y < 237 and escolha[8][3]: #9-d
                                sair = True
                                fimdejogo = False

            if telafinal:
                fundo.fill(corfundo)
                texto("Parabéns", vermelho, 50, 65, 30)
                texto("Você é um excelênte", preto, 30, 40, 80)
                texto("programador", preto, 30, 40, 100)
                pygame.display.update()
            if finale:
                if telamorte:
                    fundo.fill(corfundo)
                    texto("Fim de jogo", vermelho, 50, 65, 30)
                    texto("Pontuação Final: " + str(pontos), preto, 30, 70, 80)
                    pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
                    texto("Continuar", branco, 30, 50, 125)
                    pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
                    texto("Sair", branco, 30, 195, 125)
                    pygame.display.update()
                if not telamorte and finale:
                    perguntas(pergunta)
        # movimentação cobra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
        # questão estetica do código para o fim de jogo
        if sair:
            fundo.fill(corfundo)
            pos_x += velocidade_x
            pos_y += velocidade_y

            # posicionamento da maça
            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura - tamanho, 10)
                maca_y = randrange(0, altura - tamanho - 40, 10)
                CobraComp += 1
                pontos += 1
                if pontos == 27:
                    fimdejogo = True
                    sair = True
                    telamorte = False
                    telafinal = True
                    finale = False
                if pontos % 3 == 0:
                    pergunta += 1
                    telamorte = False
                    fimdejogo = True

            if despausar:
                # Regras de parede
                if pos_x + tamanho > largura:
                    pos_x = 0
                if pos_x < 0:
                    pos_x = largura - tamanho
                if pos_y + tamanho > altura - placar:
                    pos_y = 0
                if pos_y < 0:
                    pos_y = altura - tamanho - placar

                CobraInicio = []
                CobraInicio.append(pos_x)
                CobraInicio.append(pos_y)
                CobraXY.append(CobraInicio)
                if len(CobraXY) > CobraComp:
                    del CobraXY[0]
                # fim de jogo, colisão da cobra com sí própria
                if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                    fimdejogo = True
                    telamorte = True

                pygame.draw.rect(fundo, preto, [0, altura - placar, largura, placar])
                texto("Pontuação: " + str(pontos), branco, 20, 10, altura - 30)
                cobra(CobraXY)
                maca(maca_x, maca_y)
                pygame.display.update()
                relogio.tick(20)


jogo()
pygame.quit()
