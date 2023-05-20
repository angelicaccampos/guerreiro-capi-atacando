import pygame

# Inicialização
pygame.init()

# Medidas da tela
largura_tela, altura_tela = (1000, 720)

# Tela  
tela = (pygame.display.set_mode((largura_tela, altura_tela)))

#classe do personagem
class Guerreiro():
    #função para iniciar
    def __init__(self, x, y):
        '''
        self é uma referência ao próprio objeto da classe.
        Rect representa um retângulo e é usada para realizar operações relacionadas a posicionamento e colisão em jogos.
        O atributo self.rect é usado para definir a posição e o tamanho do retângulo que envolve o personagem.
        '''
        self.rect = pygame.Rect((x, y, largura_tela, altura_tela)) 
        self.parado = 0 # reiniciando os frames para o primeiro frames na lista de frames de parado
        self.atacar = 0 # reiniciando os frames para o primeiro frames na lista de frames de atacando

    # Função para rodar as sprites como parado ou atacando
    def desenhar(self,dicionario):
        personagem_imgagem = dicionario['parado'][self.parado] # Pega imagem atual do personagem na posição parado
        self.parado += 1 # Incrementa a próxima imagem
        
        # Ficar parado
        if self.parado == len(dicionario['parado']): # Verifica a quantidade de frames
            self.parado = 0 # Reinicia a animação para a primeira imagem na lista anições parado

        # Para atacar
        if self.atacar != 0: # Verifica se o personagem não está em estado de ataque
            if self.atacar < len(dicionario['atacando']):
                personagem_imgagem = dicionario['atacando'][self.atacar] # Obtém as imagens do personagem na posição de ataque
                self.atacar += 1 # Incrementa a próxima imagem de animação
            else:
                self.atacar = 0    # Reinicia a animação
                
        '''
        pygame.key.get_pressed() é uma função da biblioteca pygame que retorna o estado de todas 
        as teclas do teclado no momento em que é chamada. 
        '''             
        # para atacar com a barra de espaço
        if (pygame.key.get_pressed()[pygame.K_SPACE]): # Verifica se a tecla de espaço foi pressionada
            personagem_imgagem = dicionario['atacando'][self.atacar] # Obtém as imagens atual do personagem na posição de ataque
            self.atacar = 1 # Define a próxima imagem 
        else:
            self.atacar = 0 # Reinicia a animação
        # Desenha a imagem do personagem na tela na posição
        tela.blit(personagem_imgagem, self) 
        '''
        blit é um método da superfície (surface) em Pygame, usado para desenhar uma imagem
        (ou outra superfície) em outra superfície.
        '''
        
# Variáveis para guardar as coordenadas da posição inicial
x , y = (300,200)

# Variável para guardar a classe e as coordenadas da posição inicial
personagem = Guerreiro(x,y)

# função para carregar as sprites
def carregar_sprites(self):
        # Lista de animações de sprites do Guerreiro
        guerreiro_sprites_lista = [
            pygame.image.load("imagens\personagem\parado.png"),   # animações Parado
            pygame.image.load("imagens\personagem\Atacando.png")  # animações Atacando
        ]
        
        # Dicionário para cada item da lista
        guerreiro_dicionario = {'parado': [], 'atacando': []}
        
        # Pegar a altura e largura das sprites sheets
        for x, tipo in enumerate(guerreiro_dicionario): # Percorre os itens do dicionário guerreiro_dicionario, x representa o índice do item na lista 
            sheet_largura = guerreiro_sprites_lista[x].get_width() #recebe a largura da imagem  
            sheet_altura = guerreiro_sprites_lista[x].get_height() #recebe a altura da imagem  
             
            # Percorrer todas as animações e separar cada animação das sprites sheets, altura por largura
            for i in range(int(sheet_largura / sheet_altura)): # Para determinar o número de animações 
                img = guerreiro_sprites_lista[x].subsurface( i * sheet_altura, 0, sheet_altura, sheet_altura)
                guerreiro_dicionario[tipo].append(pygame.transform.scale(img, (sheet_altura, sheet_altura)))
        return guerreiro_dicionario

# Variável auxiliar para guardar a função carregar_sprites
guerreiro = carregar_sprites(self = any)

# Função para desenhar o fundo
def desenhar_fundo():
    fundo = pygame.image.load("imagens\Fundo\Fundo.jpg")  # Fundo qualquer
    fundo_ajustado = pygame.transform.scale(fundo, (largura_tela, altura_tela))
    tela.blit(fundo_ajustado, (0,0))

# Rodar o jogo
jogando = True
while jogando:
    '''
    pygame.time.Clock().tick(5) é usada para limitar a taxa de atualização do jogo a um certo número
    de quadros por segundo (FPS).
    '''
    pygame.time.Clock().tick(5)
    
    #chamando a função do fundo
    desenhar_fundo()
    
    #chamando a função que desenha as sprites
    personagem.desenhar(guerreiro)
    
    #sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    pygame.display.flip()
pygame.quit