import pygame
from classes import *


pygame.init()

window = pygame.display.set_mode((800, 600))

entitys = [

]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))

    for individual in entitys:
        individual.update()
    
    pygame.display.flip()