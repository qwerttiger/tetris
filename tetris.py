import os #import os, a tool for finding files and
import pygame,sys #import pygame and sys, a tool for exiting
pygame.init() #initiate pygame
screen=pygame.display.set_mode((700,700)) #setup display
pygame.display.set_caption("Tetris") #set caption
tetrislogo=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/tetris/pictures/tetrislogo.png") #load tetris logo
play=pygame.image.load("C:/Users/Rainbow/Documents/GitHub/tetris/pictures/play.png") #load play button
screen.fill((50,50,50)) #fill screen
screen.blit(tetrislogo,(350-tetrislogo.get_width()/2,100-tetrislogo.get_height()/2)) #draw the tetris logo
screen.blit(play,((350-play.get_width()/2,600-play.get_height()/2))) #draw the play button
keep_going=True #set keep going to True
def load(names):
  for name in names:
    name_=f"C:/Users/Rainbow/Documents/GitHub/tetris/pictures/{name}.png"
    exec(f"global {name}")
    exec(f"{name}=pygame.image.load('{name_}')",globals())
listofblocks=[]
for root,_,files in os.walk("C:/Users/Rainbow/Documents/GitHub/tetris/pictures"):
  for file in files:
    if file not in ["play.png","tetrislogo.png"]:
      listofblocks+=[file[:-4]]
load(listofblocks)
while keep_going: #while you are keep going
  for event in pygame.event.get(): #for every event
    if event.type==pygame.QUIT: #if the type is quit
      pygame.quit() #quit
    if event.type==pygame.MOUSEBUTTONDOWN: #if you click
      pos=pygame.mouse.get_pos() #set pos to be the position of the mouse
      if pos[0]>=350-play.get_width()/2 and pos[0]<=350+play.get_width()/2 and pos[1]>=600-play.get_height()/2 and pos[1]<=600+play.get_height()/2: #if you click on the button
        keep_going=False #stop going
  pygame.display.flip() #update screen
screen.fill((50,50,50))
pygame.display.flip()
