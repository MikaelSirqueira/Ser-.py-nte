''' A biblioteca pygame é importada, 
juntamente do modulo locals dela, além 
disso o metodo randrange que usaremos 
para gerar numeros aleatórios para as 
posições da cobra e maçã '''
import pygame
import pygame.locals
from random import randrange

print("Módulos importados com sucesso")

''' Utilizando um bloco de tentativa e erro
para checar se o pygame foi iniciado corretamente '''
try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")

''' Declaração das váriaveis globais que utilizaremos
em todo o código, altura e largura da tela, tamanho da
cobra e maçã, tamanho do placar e cores no formato RGB'''
largura = 640
altura = 480
tamanho = 20
placar = 40
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 200, 0)
verde_escuro = (0, 150, 0)
azul = (0, 0, 255)
prata = (192, 192, 192)
laranja = (255, 69, 0)
cinza = (79, 79, 79)
cinzaClaro = (220, 220, 220)

''' Definição de configurações do jogo, relógio para
definir o fps, fundo para desenhar tudo do jogo e o 
título da janela do jogo '''
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

''' Classe texto servirá para criar objetos de textop
que serão exibidos nas telas do jogo, recebe a mensagem
a cor e o tamanho como parâmetros '''


class Texto:
    def __init__(self, msg, cor, tam):
        self.font = pygame.font.SysFont(None, tam)
        self.texto = self.font.render(msg, True, cor)

    ''' Método mostrar desenha na tela o texto criado pelo
    construtor da classe '''

    def mostrar(self, x, y):
        fundo.blit(self.texto, [x, y])


''' Classe cobra definirá os elementos do objeto
cobra, como cabeça, comprimento e direção, bem
como o array que contém a posição de cada pedaço
da cobra, recebe as coordenadas x e y como parâmetro, 
que será o local na tela onde ela começará o jogo '''


class Cobra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cabeca = [x, y]
        self.comp = 1
        self.cobra = [self.cabeca]
        self.direcao = ""

    ''' Método move, recebe os parâmetro x e y,
    que serão as novas coordenadas da cabeça e 
    insere a nova cabeça no array das posições '''

    def move(self, x, y):
        self.cabeca = [x, y]
        self.cobra.append([x, y])

    ''' Método cresce, aumenta o comprimento da
    cobra '''

    def cresce(self):
        self.comp += 1

    ''' Método mostrar, desenha cada pedaço da cobra
    na tela '''

    def mostrar(self):
        indice = 0
        for XY in self.cobra:
            if indice == len(self.cobra) - 1:
                pygame.draw.rect(fundo, verde_escuro, [XY[0], XY[1], tamanho, tamanho])
            else:
                pygame.draw.rect(fundo, verde, [XY[0], XY[1], tamanho, tamanho])
            indice += 1

    ''' Método rastro, remove a cauda quando o
    tamanho do array é maior que o comprimento da
    cobra '''

    def rastro(self):
        if len(self.cobra) > self.comp:
            del self.cobra[0]

    ''' Método morreu, verifica se a cobra comeu
    ela mesma, se sim retorna verdadeiro, caso 
    contrário, retorna falso '''

    def morreu(self):
        if any(Bloco == self.cabeca for Bloco in self.cobra[:-1]):
            return True
        return False

    ''' Método reinicia, redefine todos os valores 
    da cobra para os valores iniciais, para caso
    depois de ter perdido o jogados possa continuar
    jogando '''

    def reinicia(self, x, y):
        self.x = x
        self.y = y
        self.cabeca = [x, y]
        self.comp = 1
        self.cobra = [self.cabeca]


''' Classe maçã que definirá o objeto maçã,
não recebe nenhum parâmetro, possui os atributos
x e y que é a posição da maçã na tela '''


class Maca:
    def __init__(self):
        self.x = randrange(0, largura - tamanho, 20)
        self.y = randrange(0, altura - tamanho - placar, 20)

    ''' Método mostrar, desenha a maçã na tela '''

    def mostrar(self):
        pygame.draw.rect(fundo, vermelho, [self.x, self.y, tamanho, tamanho])

    ''' Método reposicionar, define novos x e y
    aleatórios para a maçã após ser comida pela cobra '''

    def reposicionar(self):
        self.x = randrange(0, largura - tamanho, 20)
        self.y = randrange(0, altura - tamanho - placar, 20)


''' Classe Jogo, definirá todo o restante do jogo, 
como variaveis de controle para continuar jogando,
perder, posição e velocidade da cobra, pontos, bem como
são criados os objetos maçã e cobra, não recebe parâmetros '''


# noinspection DuplicatedCode
class Jogo:
    def __init__(self):
        self.jogando = False
        self.perdeu = False
        self.noMenu = True
        self.modo = None

        self.fundo = preto

        self.pos_x = randrange(0, largura - tamanho, 20)
        self.pos_y = randrange(0, altura - tamanho - placar, 20)

        self.velocidade_x = 0
        self.velocidade_y = 0

        self.pontos = 0

        self.cobra = Cobra(self.pos_x, self.pos_y)
        self.maca = Maca()

    ''' Método iniciar, possui o loop principal do jogo,
    que faz absolutamente tudo que acontece no jogo '''

    def iniciar(self):
        pontos_fundo = 0
        while self.jogando:

            ''' Iterador de eventos, todos os eventos que
            acontecem durante o tempo de execução estão podem
            ser obtidos pelo "pygame.event.get()", sendo assim 
            verificado se o jogo não foi fechado, bem como se
            nenhuma das setas foi apertada para mover a cobra '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.cobra.direcao != "direita":
                        self.cobra.direcao = "esquerda"
                    if event.key == pygame.K_RIGHT and self.cobra.direcao != "esquerda":
                        self.cobra.direcao = "direita"
                    if event.key == pygame.K_UP and self.cobra.direcao != "baixo":
                        self.cobra.direcao = "cima"
                    if event.key == pygame.K_DOWN and self.cobra.direcao != "cima":
                        self.cobra.direcao = "baixo"
                    if event.key == pygame.K_SPACE:
                        self.pontos += 1
                        pontos_fundo += 1
                        self.cobra.cresce()

            ''' Checa se o jogador ainda não perdeu o jogo '''
            if self.jogando:

                ''' Descomente e descubra o que isso faz'''
                # if pontos_fundo == 10:
                #     pontos_fundo = 0
                #     if self.fundo == branco:
                #         self.fundo = preto
                #     else:
                #         self.fundo = branco

                ''' Limpa a tela a cada novo inicio de loop '''
                fundo.fill(self.fundo)
                ''' Checa para qual direção a cobra está seguindo e 
                redefine a nova posição naquela direção '''
                if self.cobra.direcao == "cima":
                    self.pos_y -= tamanho
                elif self.cobra.direcao == "baixo":
                    self.pos_y += tamanho
                elif self.cobra.direcao == "esquerda":
                    self.pos_x -= tamanho
                elif self.cobra.direcao == "direita":
                    self.pos_x += tamanho
                else:
                    pass

                ''' Checa se a cobra e a maçã estão na mesma posição,
                caso estejam, a maçã é reposicionada, a cobra aumenta e
                o placar de pontos aumenta '''
                if self.pos_x == self.maca.x and self.pos_y == self.maca.y:
                    self.maca.reposicionar()
                    self.cobra.cresce()
                    self.pontos += 1
                    pontos_fundo += 1

                ''' Aqui primeiro é feita a checagem do modo, caso o modo 
                escolhido no menu tenha sido o modo livre, o jogo não possuirá
                 bordas e você poderá atravessar o mapa, mas caso tenha escolhido
                 o modo clássico é checado se a cobra ultrapassou alguma das bordas,
                caso tenha ultrapassado é definido que não se está
                mais jogando porque perdeu e é chamado o método "perdido" '''
                if self.modo == "livre":
                    if self.pos_x + tamanho > largura:
                        self.pos_x = 0
                    if self.pos_x < 0:
                        self.pos_x = largura - tamanho
                    if self.pos_y + tamanho > altura - placar:
                        self.pos_y = 0
                    if self.pos_y < 0:
                        self.pos_y = altura - tamanho - placar
                else:
                    pygame.draw.rect(fundo, branco, [0, 0, 2, altura])
                    pygame.draw.rect(fundo, branco, [0, 0, largura, 2])
                    pygame.draw.rect(fundo, branco, [largura - 2, 0, 2, altura])
                    pygame.draw.rect(fundo, branco, [0, altura - placar - 2, largura, 2])
                    if self.pos_x + tamanho > largura:
                        self.jogando = False
                        self.perdeu = True
                        self.perdido()
                    if self.pos_x < 0:
                        self.jogando = False
                        self.perdeu = True
                        self.perdido()
                    if self.pos_y + tamanho > altura - placar:
                        self.jogando = False
                        self.perdeu = True
                        self.perdido()
                    if self.pos_y < 0:
                        self.jogando = False
                        self.perdeu = True
                        self.perdido()

                ''' Move a cobra para a nova posição que é 
                definida como parâmetro do método '''
                self.cobra.move(self.pos_x, self.pos_y)

                ''' Limpa o rastro deixado pelo blocos adicionais '''
                self.cobra.rastro()

                ''' Checa se a cobra comeu ela mesma, caso
                tenha comido o jogo é definido perdido, e o 
                método "perdido" é chamado '''
                if self.cobra.morreu():
                    self.jogando = False
                    self.perdeu = True
                    self.perdido()

                ''' Desenha a cobra na tela '''
                self.cobra.mostrar()

                ''' Desenha o placar e o texto contendo a pontuação atual '''
                pygame.draw.rect(fundo, branco, [0, altura - placar, largura, placar])
                textoPlacarSombra = Texto("Pontuação:" + str(self.pontos), cinza, 25)
                textoPlacarSombra.mostrar(9, altura - 31)
                textoPlacar = Texto("Pontuação:" + str(self.pontos), branco, 25)
                textoPlacar.mostrar(10, altura - 30)

                ''' Desenha a maçã na tela '''
                self.maca.mostrar()

                ''' Atualiza toda a tela com todos os
                elementos que foram desenhados anteriormente '''
                pygame.display.update()

                ''' Define o fps do jogo '''
                relogio.tick(15)

    ''' Método perdido, possui o loop da tela de
    derrota, faz tudo que acontece ao perder, 
    podendo o jogador voltar a jogar ou sair do jogo '''

    def perdido(self):
        while self.perdeu:

            ''' Iterador de eventos, todos os eventos que
            acontecem durante o tempo de execução estão podem
            ser obtidos pelo "pygame.event.get()", é verificado
            se o jogador quis sair do jogo ou quer voltar a jogar,
            caso queira voltar, todo o jogo é redefinido e se retorna
            para o método iniciar '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    self.perdeu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.jogando = False
                        self.perdeu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_x = mouse_pos[0]
                    mouse_y = mouse_pos[1]
                    if 143 < mouse_x < 143 + 369 and 168 < mouse_y < 168 + 51:
                        self.jogando = False
                        self.perdeu = False
                        self.noMenu = True
                        self.pos_x = randrange(0, largura - tamanho, 20)
                        self.pos_y = randrange(0, altura - tamanho - placar, 20)
                        self.cobra.direcao = ""
                        self.maca.reposicionar()
                        self.cobra.reinicia(self.pos_x, self.pos_y)
                        self.velocidade_x = 0
                        self.velocidade_y = 0
                        self.pontos = 0
                    if 193 < mouse_x < 193 + 279 and 268 < mouse_y < 268 + 58:
                        self.jogando = True
                        self.perdeu = False
                        self.pos_x = randrange(0, largura - tamanho, 20)
                        self.pos_y = randrange(0, altura - tamanho - placar, 20)
                        self.cobra.direcao = ""
                        self.maca.reposicionar()
                        self.cobra.reinicia(self.pos_x, self.pos_y)
                        self.velocidade_x = 0
                        self.velocidade_y = 0
                        self.pontos = 0

            ''' Limpa a tela '''
            fundo.fill(branco)

            ''' Desenha "Voce Perdeu" na tela '''
            textoPerdeuSombra = Texto("Você Perdeu", cinza, 80)
            textoPerdeuSombra.mostrar(159, 29)
            textoPerdeu = Texto("Você Perdeu", vermelho, 80)
            textoPerdeu.mostrar(160, 30)

            ''' Desenha a pontuação final do jogador '''
            textoPontuacaoSombra = Texto("Pontuação Final: " + str(self.pontos), cinza, 50)
            textoPontuacaoSombra.mostrar(179, 99)
            textoPontuacao = Texto("Pontuação Final: " + str(self.pontos), prata, 50)
            textoPontuacao.mostrar(180, 100)

            ''' Desenha o botão de voltar ao menu de seleção '''
            pygame.draw.rect(fundo, prata, [143, 168, 369, 51])
            pygame.draw.rect(fundo, preto, [145, 170, 365, 47])
            textoContinuar = Texto("Voltar ao Menu", branco, 70)
            textoContinuar.mostrar(150, 173)

            ''' Desenha o botão de continuar jogando '''
            pygame.draw.rect(fundo, prata, [193, 268, 279, 58])
            pygame.draw.rect(fundo, preto, [195, 270, 275, 54])
            textoContinuar = Texto("Novo Jogo", branco, 70)
            textoContinuar.mostrar(210, 273)

            ''' Atualiza a tela com todos os elementos '''
            pygame.display.update()

    def menu(self):
        while self.noMenu:

            ''' Iterador de eventos, todos os eventos que
            acontecem durante o tempo de execução estão podem
            ser obtidos pelo "pygame.event.get()", é verificado
            se o jogador quis sair do jogo ou quer voltar a jogar,
            caso queira voltar, todo o jogo é redefinido e se retorna
            para o método iniciar '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.noMenu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.noMenu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_x = mouse_pos[0]
                    mouse_y = mouse_pos[1]
                    if 143 < mouse_x < 143 + 359 and 168 < mouse_y < 168 + 51:
                        self.jogando = True
                        self.perdeu = False
                        self.noMenu = False
                        self.modo = "classico"
                        self.iniciar()
                    if 183 < mouse_x < 183 + 279 and 268 < mouse_y < 268 + 51:
                        self.jogando = True
                        self.noMenu = False
                        self.perdeu = False
                        self.modo = "livre"
                        self.iniciar()
            ''' Limpa a tela '''
            fundo.fill(branco)

            ''' Desenha o titulo "Snake Game" na tela '''
            # textoPerdeuSombra = Texto("Snake Game", cinza, 100)
            # textoPerdeuSombra.mostrar(108, 28)
            textoPerdeu = Texto("Snake Game", preto, 100)
            textoPerdeu.mostrar(110, 30)

            ''' Desenha o botão de continuar jogando '''
            pygame.draw.rect(fundo, prata, [143, 168, 359, 51])
            pygame.draw.rect(fundo, preto, [145, 170, 355, 47])
            textoContinuar = Texto("Modo Clássico", branco, 70)
            textoContinuar.mostrar(150, 173)

            ''' Desenha o botão de continuar jogando '''
            pygame.draw.rect(fundo, prata, [183, 268, 279, 51])
            pygame.draw.rect(fundo, preto, [185, 270, 275, 47])
            textoContinuar = Texto("Modo Livre", branco, 70)
            textoContinuar.mostrar(190, 273)

            ''' Atualiza a tela com todos os elementos '''
            pygame.display.update()


''' Instancia do jogo '''
if __name__ == '__main__':
    instancia = Jogo()
    instancia.menu()  # Iniciando o jogo através da instância

''' Fecha a janela principal do jogo '''
pygame.quit()