import pygame #import pygame
pygame.init() #initiate pygame
screen=pygame.display.set_mode((700,700)) #setup display
pygame.display.set_caption("Tetris") #set caption
tetrislogo=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/tetris/pictures/tetrislogo.png")
screen.fill((50,50,50))
pygame.display.flip()
