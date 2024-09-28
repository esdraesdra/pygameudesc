import pygame               ##importa tudo
from pygame import display,event,font  ##importa apenas um recurso
from pygame.locals import QUIT
from pygame.time import Clock
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import GroupSingle, Group

import botao
from jogador import Jogador
from inimigo import Inimigo
#pygame.display.set_mode((0,0),pygame.FULLSCREEN)

class Jogo(): ##classe
    def __init__(self): ##metodo
            pygame.init()
            self.esta_rodando = True
            self.estado = 0
            self.tamanho = 800,600
            self.superficie = display.set_mode(
                size = self.tamanho,
                display = 0
            )
            display.set_caption(
                'Ship Shoot'
            )
            self.font_destaque = font.SysFont(
                'comicsans',
                80,
                True,
                True
            )

            self.imagem_inicio = pygame.image.load('images/button_inicio.png').convert_alpha()
            self.imagem_sair = pygame.image.load('images/button_sair.png').convert_alpha()
            self.botao_inicio = botao.Botao(30,450,self.imagem_inicio,0.8)
            self.botao_sair = botao.Botao(600,450,self.imagem_sair,0.8)

            self.clock = Clock()
            self.fundo = scale(
                load('images/space.jpg'),
                self.tamanho
            )

    def novo_jogo(self):
        self.group_inimigos = Group()
        self.jogador = Jogador(self)
        self.group_jogador = GroupSingle(self.jogador)
        self.group_inimigos.add(Inimigo(self))
        self.round = 0

    def rodar(self): #metodo
        while self.esta_rodando: ##enquanto esta_rodando for true
            for evento in event.get():
                if evento.type == QUIT:
                    self.esta_rodando = False ##fechar o jogo
            if self.estado == 0:
                self.superficie.fill((50,50,255)) ##fundo
                titulo = self.font_destaque.render( #titulo sem .self pq n quero usar dps
                    'Ship Shoot',
                    True,
                    (255,165,0)
                )
                self.superficie.blit(titulo,(190,180))
                if self.botao_inicio.criar(self.superficie):
                    print('start')
                    self.estado = 1
                    self.novo_jogo()
                if self.botao_sair.criar(self.superficie):
                    self.esta_rodando = False

            elif self.estado == 1:
                self.clock.tick(120)
                self.superficie.blit(self.fundo,(0,0))
                self.group_jogador.draw(self.superficie)
                self.group_jogador.update()
                self.group_inimigos.draw(self.superficie)

            display.update() ##vai atualizar a tela a cada vez que o jogo rodar "algo acontecer"
    
g = Jogo() ##receber instancia do jogo
g.rodar() #chamando o metodo rodar
pygame.quit()
exit()