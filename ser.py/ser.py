import pygame
import random as rd

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

try:
    pygame.init()
except:
    print("O modulo pygame nÃ£o foi inicializado com sucesso")

largura=640
altura=480
tamanho = 10
placar = 40

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

font = pygame.font.Sysfont(None,25)

def texto(msg, cor, tam, x, y):
    font = pygame.font.Sysfont(None,25)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(CobraXY):
  for XY in CobraXY:
    pygame.draw.rect([XY[0], XY[1], tamanho, tamanho])

def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])

def jogo():
    sair = True
    fimdejogo = False
    pos_x=rd.randrange(0,largura-tamanho,10)
    pos_y=rd.randrange(0,altura-tamanho-placar,10)
    maca_x=rd.randrange(0,largura-tamanho,10)
    maca_y=rd.randrange(0,altura-tamanho-placar,10)
    velocidade_x=0
    velocidade_y=0
    CobraXY = []
    CobraComp = 1
    pontos = 0
    while sair:
      while fimdejogo:
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sair = False
            fimdejogo = False
          if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT_C:
                  sair = True
                  fimdejogo = False
                  pos_x=rd.randrange(0,largura-tamanho,10)
                  pos_y=rd.randrange(0,altura-tamanho-placar,10)
                  maca_x=rd.randrange(0,largura-tamanho,10)
                  maca_y=rd.randrange(0,altura-tamanho-placar,10)
                  velocidade_x=0
                  velocidade_y=0
                  CobraXY = []
                  CobraComp = 1
                  pontos = 0
                if event.key == pygame.K_LEFT_S:
                  sair = False
                  fimdejogo = False

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
            if event.type == pygame.MOUSEBUTTONDOWN:
              x = pygame.mouse.get_pos()[0]
              y = pygame.mouse.get_pos()[1]
              if x > 45 and y > 120 and x < 180 and y < 147:
                        sair = True
                        fimdejogo = False
                        pos_x = rd.randrange(0, largura - tamanho, 10)
                        pos_y = rd.randrange(0, altura - tamanho - placar, 10)
                        maca_x = rd.randrange(0, largura - tamanho, 10)
                        maca_y = rd.randrange(0, altura - tamanho - placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        sair = True
                        fimdejogo = False

              
        fundo.fill(branco)
        texto("Fim de jogo", vermelho, 50, 65, 30)
        texto("Pontuação Final: " + str(pontos), preto, 30, 70, 80)
        pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
        texto("Continuar (C)", branco, 30, 50, 125)
        pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
        texto("Sair (S)",branco, 30, 50, 125 )
        pygame.display.update()
      if sair: 
          fundo.fill(branco)
          pos_x+=velocidade_x
          pos_y+=velocidade_y
          
          if pos_x + tamanho> largura:
              pos_x = 0
          if pos_x < 0:
              pos_x=largura-tamanho
          if pos_y + tamanho> altura-placar:
              pos_y = 0
          if pos_y < 0:
              pos_y= altura-tamanho-placar

          
          CobraInicio = []
          CobraInicio.append(pos_x)
          CobraInicio.append(pos_y)
          CobraXY.append(CobraInicio)
          if len(CobraXY) > CobraComp:
            del CobraXY[0]
          if any (Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo = True


        pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])
        texto("Pontuação: ")
          cobra(CobraXY)
          if pos_x == maca_y and pos_y == maca_y:
            maca_x=rd.randrange(0,largura-tamanho,10)
            maca_y=rd.randrange(0,altura-tamanho-placar,10)
            pontos += 1