import pygame
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((626,417))

fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

import random
x_random = random.randint(100,400)
y_random = random.randint(30,300)
boat = pygame.image.load("boat.png").convert_alpha()
position_boat = fenetre.blit(boat, (x_random, y_random))

pygame.display.flip()


continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == MOUSEBUTTONDOWN:
            if boat.collidepoint("boat.png"):
                position_boat = fenetre.blit(boat, (x_random, y_random))

fenetre.blit(fond, (0,0))

pygame.display.flip()
