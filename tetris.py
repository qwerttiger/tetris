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
  x=random.choice("O left right tleft tright I tI L lL fL rL oL loL foL roL t rt ft lt".split())
  a=eval(x)
  a.set_colorkey((255,255,255))
  return a,x
class matrix:
  def __init__(self,string=(("0"*10+"\n")*20)[:-1]):
    self.matrix=[[int(y) for y in x] for x in string.split("\n")]
    self.x=len(self.matrix[0])
    self.y=len(self.matrix)
  def getat(self,xpos,ypos):
    try:
      if xpos>=0 and ypos>=0:
        return self.matrix[ypos][xpos]
      else:
        return matrix("")
    except:
      return matrix("")
  def setat(self,xpos,ypos,yes=1):
    try:
      if xpos>=0 and ypos>=0:
        self.matrix[ypos][xpos]=yes
    except:
      pass
  def collide(self,other,diff):
    for ypos1 in range(20):
      for xpos1 in range(10):
        xpos2=xpos1-diff[0]
        ypos2=ypos1-diff[1]
        if self.getat(xpos1,ypos1)==1 and other.getat(xpos2,ypos2)==1:
          return True
    return False
  def clear(self):
    self.matrix=[[0]*len(self.matrix[0])]*len(self.matrix)
  def add(self,other,diff):
    for ypos in range(20):
      for xpos in range(10):
        if other.getat(xpos-diff[0],ypos-diff[1])==1:
          self.setat(xpos,ypos,1)
  
        
def draw(blocks):
  a=blocks[0][0]
  b=blocks[1][0]
  c=blocks[2][0]
  d=blocks[3][0]
  nextsurface.blit(a,(50-a.get_width()/2,50-a.get_height()/2))
  nextsurface.blit(b,(50-b.get_width()/2,150-b.get_height()/2))
  nextsurface.blit(c,(50-c.get_width()/2,250-c.get_height()/2))
  nextsurface.blit(d,(50-d.get_width()/2,350-d.get_height()/2))
def getmatrix(block):
  block=block[1]
  def cond(block,listt):
    for x in listt:
      if block==x[0]:
        return matrix(x[1])
  return cond(block,(("O","11\n11"),("left","10\n11\n01"),("right","01\n11\n10"),("tleft","011\n110"),("tright","110\n011"),("I","1\n1\n1\n1"),("tI","1111"),("L","10\n10\n11"),("rL","111\n100"),("fL","11\n01\n01"),("lL","001\n111"),("oL","01\n01\n11"),("roL","100\n111"),("foL","11\n10\n10"),("loL","111\n001"),("t","111\n010"),("rt","01\n11\n01"),("ft","010\n111"),("lt","10\n11\n10")))
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
      sys.exit() #exit
    if event.type==pygame.MOUSEBUTTONDOWN: #if you click
      pos=pygame.mouse.get_pos() #set pos to be the position of the mouse
      if pos[0]>=350-play.get_width()/2 and pos[0]<=350+play.get_width()/2 and pos[1]>=600-play.get_height()/2 and pos[1]<=600+play.get_height()/2: #if you click on the button
        keep_going=False #stop going
  pygame.display.flip() #update screen
screen.fill((50,50,50))
pygame.display.flip()
keep_going=True
screenmatrix=matrix()
blocks=[randomblock(),randomblock(),randomblock(),randomblock()]
currentblock=randomblock()
nextsurface=pygame.Surface((100,400))
matrixscreen=pygame.Surface((100,200))
alreadymatrix=pygame.Surface((100,200))
alreadymatrix.fill((255,255,255))
alreadymatrix.set_colorkey((255,255,255))
while keep_going:
  screen.fill((50,50,50))
  nextsurface.fill((100,100,100))
  matrixscreen.fill((255,255,255))
  currentblock=blocks.pop(0)
  blocks+=[randomblock()]
  draw(blocks)
  screen.blit(nextsurface,(550,50))
  screen.blit(matrixscreen,(300,250))
  blockmatrix=getmatrix(currentblock)
  xpos=random.randint(0,10-currentblock[0].get_width()/10)*10
  ypos=0
  yes=4
  while yes==4:
    matrixscreen.fill((255,255,255))
    matrixscreen.blit(currentblock[0],(round(xpos/10)*10,round(ypos/10)*10))
    screen.blit(matrixscreen,(300,250))
    screen.blit(alreadymatrix,(300,250))
    ypos+=0.1
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and xpos>=0:
      xpos-=0.1
    if pressed[pygame.K_RIGHT] and xpos<=100-currentblock[0].get_width():
      xpos+=0.1
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.flip()
    yes=0
    for x in range(5,105,10):
      for y in range(5,205,10):
        if not matrixscreen.get_at((x,y))==(255,255,255,255):
          yes+=1
    if screenmatrix.collide(blockmatrix,(round(xpos/10),round((ypos-1)/10))):
      break
  
  screenmatrix.add(blockmatrix,(round(xpos/10),round((ypos-1)/10)))
  alreadymatrix.blit(currentblock[0],(round(xpos/10)*10,round(ypos/10)*10-10))
