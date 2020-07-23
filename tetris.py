import os #import os, a tool for finding files and not letting python write support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide" #hide support prompt
import pygame,sys,random #import pygame and sys, a tool for exiting, and random, a tool for random choices
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
def randomblock():
  return random.choice("O left right tleft tright I tI L lL fL rL oL loL foL roL t rt ft lt".split())
class matrix:
  def __init__(self,string):
    self.matrix=[[int(y) for y in x] for x in string.split("\n")]
    self.x=len(self.matrix[0])
    self.y=len(self.matrix)
  def getat(self,xpos,ypos):
    try:
      return self.matrix[ypos][xpos]
    except:
      return matrix("")
  def collide(self,other,diff):
    for ypos1 in range(20):
      for xpos1 in range(10):
        xpos2=xpos1+diff[0]
        ypos2=ypos1+diff[1]
        if self.getat(xpos1,ypos1)==other.getat(xpos2,ypos2):
          return True
    return False
  def clear(self):
    self.matrix=[[0]*len(self.matrix[0])]*len(self.matrix)
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
      sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN: #if you click
      pos=pygame.mouse.get_pos() #set pos to be the position of the mouse
      if pos[0]>=350-play.get_width()/2 and pos[0]<=350+play.get_width()/2 and pos[1]>=600-play.get_height()/2 and pos[1]<=600+play.get_height()/2: #if you click on the button
        keep_going=False #stop going
  pygame.display.flip() #update screen
screen.fill((50,50,50))
pygame.display.flip()
keep_going=True
screenmatrix=matrix("")
screenmatrix.clear()
while keep_going:
  for event in pygame.event.get():
    pass
