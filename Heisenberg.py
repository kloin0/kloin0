import pygame 
import random 
from pygame.locals import * 
from sys import exit 
pygame.init()
x = 500 
y = 500 
tela = pygame.display.set_mode((x,y))
pygame.display.set_caption("Heisenberg")
relogio = pygame.time.Clock()
def Heisenberg():
    h = 0 
    while 1:
        relogio.tick(1000000*10000000*1000000*1000000*1000000*1000000*1000000*1000000*1000000*1000000*1000000*10000000*10000000)
        px = random.randint(100,400)
        py = random.randint(100,400)
        tela.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                exit()
        pygame.draw.circle(tela,(40,45,50),(px,py),20)
        h += 1 
        print(f'{h}- *px: {px}, f*py: {py}')
        pygame.display.update()
Heisenberg()
