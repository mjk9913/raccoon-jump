"""
This project was created by Team White (Rock, Avani, Min Jie)
All graphics were created by Rock
Raccoon Jump
"""

add_library("minim")
player = Minim(this)
RESX= 600
RESY=800
import random
import os
path=os.getcwd()
widthtree = 80

records = open("highscore.csv", "r") #open csv file for max score recorded
highscore = 0

for i in records: #Loop to determine max score
    record = int(i.strip())
    if record is None:
        continue
    if highscore <= record:
        highscore = record

records.close()
class before:
    
    def __init__(self):
        self.play=0
        self.img=5
        self.img0=loadImage(path + "/images/" + "raccoonstart0.png") #raccon choice 1
        self.img1=loadImage(path + "/images/" + "raccoonstart1.png") #raccon choice 2
        self.img2=loadImage(path + "/images/" + "raccoonstart2.png")#raccon choice 3 
        self.img3=loadImage(path + "/images/" + "raccoonstart3.png")#raccon choice 4
        self.startbg = loadImage(path + "/images/" + "startingscreen.png")
        self.button = loadImage(path + "/images/" + "startbutton.png")
        self.counter = False
    
        
        
    def display(self):
        if(self.counter == False): #displaying starting screen
            image(self.startbg, 0, 0, RESX, RESY) 
            fill(250)
            image(self.button, 250, 5, 100, 50)
    
        #enabling player to only move to racoon selection screen if click on start button
        if(mousePressed == True and 250 < mouseX < 350 and 5 < mouseY < 55):
            self.counter = True
    


        if(self.play==0 and self.counter == True): #racoon selection screen
          background(46, 188, 162)
          textSize(30)
          text("Welcome to Raccoon world", 100, 100)
          fill(250)
          #rect(15,150, 270,500)
          image(self.img0, 50, 150, 210, 250,0, 0 ,700,700)
          #rect (300, 150,270, 500)
          image(self.img1, 300, 150, 210,250,0,0 ,700,700)
          image(self.img3, 50, 400, 210, 250,0, 0 ,700,700)
          image(self.img2, 300, 400, 210, 250,0, 0 ,700,700)
          
          fill(0)
          rect(150, 670, 300, 60) 
          fill(250)
          textSize(30)
          text("Choose your avatar",155,710 )
          
          
          if(50<=mouseX<=210 and 150<=mouseY<=360): 
              stroke (250,0,0) #character highlighted when mouse hovered
              strokeWeight(3)
              noFill()
              rect(50,150, 210,265)
              if(mousePressed):
                  self.img= loadImage(path + "/images/" + "racoon"+str(0)+".png")
                #setting racoon image in game as one selected
                  be.play=1 

                  return
              
              
          if(300<=mouseX<=510 and 150<=mouseY<=360):
              stroke (250,0,0) #character highlighted when mouse hovered
              strokeWeight(3)
              noFill()
              rect(300,150, 210, 265)
              if(mousePressed): #setting racoon image in game as one selected
                  self.img= loadImage(path + "/images/" + "racoon"+str(1)+".png")
            
                  be.play=1

                  return
              
          if(300<=mouseX<=510 and 360<=mouseY<=650):
              stroke (250,0,0) #character highlighted when mouse hovered
              strokeWeight(3)
              noFill()
              rect(300,400, 210, 265)
              if(mousePressed): #setting racoon image in game as one selected
                  self.img= loadImage(path + "/images/" + "racoon"+str(2)+".png")
            
                  be.play=1
                  return
              
          if(50<=mouseX<=210 and 360<=mouseY<=650):
              stroke (250,0,0) #character highlighted when mouse hovered
              strokeWeight(3)
              noFill()
              rect(50,400, 210, 265)
              if(mousePressed): #setting racoon image in game as one selected
                  self.img= loadImage(path + "/images/" + "racoon"+str(3)+".png")
            
                  be.play=1
                  return
              
          stroke(250)
          strokeWeight(0)
          return #ending display + selection screen 
        
class Racoon:
  def __init__(self):
      self.x = widthtree+30
      self.vx = 0
      self.y = 800
      self.r = 173/2
      self.w=104
      self.h=173
      self.vy = 5
      self.blank = loadImage(path+ "/images/" + "blank.png")
      self.music = player.loadFile(path + "/swoosh.mp3")
      self.frame = 0
      self.img_total = 17
      self.blinking = False
      self.blinkingnum = 0
      self.direction = RIGHT 
      self.key_handle = {"SPACE":False}

  def switch_dir(self):
      if(self.key_handle["SPACE"] == True and game.status == True):
        self.music.rewind() 
        self.music.play() #playing swoosh music when racoon switching sides
        
        if(self.direction == RIGHT):
            self.direction = LEFT
            self.x = RESX - self.x #inversing x position of racoon
                
        else: 
            self.direction = RIGHT
            self.x = RESX - self.x #inversing x position of racoon
  
  def display(self):
    self.up()
    
    if self.blinking == True: 
        if self.blinkingnum > 60:
            self.blinking = False
            
        if self.blinkingnum%10 == 0:
            self.img = self.blank #alternating img as blank, instead of racoon, when hit by coconut to illustrate blinking
            

        self.blinkingnum += 1
    

    if(self.y<=RESY/(1.6)): #keeping the racoon in the middle of the screen
      game.y_shift-=self.vy 

    if self.direction == RIGHT: #display racoon
            image(self.img, self.x - self.w//2 , self.y - self.h//2 - game.y_shift , self.w, self.h, 0, self.frame * self.h, self.w,(self.frame + 1) * self.h)
            
    elif self.direction == LEFT: #inversing racoon image when on other side
            image(self.img, self.x - self.w//2 , self.y - self.h//2 - game.y_shift , self.w, self.h, self.w, self.frame * self.h, 0,(self.frame + 1) * self.h)
  
  def distance(self, other): #calculating distance of racoon and objects
    distance = ((self.x - other.x) ** 2 + (self.y - other.y - game.y_shift) ** 2) ** 0.5 
    return(distance)
    
  def contact(self, other): #determining if racoon and objects crashed
    d=self.distance(other)
    if(d <= self.r + other.r):
      return True
    return False
    
  def up(self):
    self.y-=self.vy #keeping racoon moving

    if frameCount%2 == 0: #changing frame of racoon image to illustrate motion
        self.frame = (self.frame + 1) % self.img_total
        
  def win(self): #prevent game.shift_y in order to allow racoon to climb up and out of screen, no longer in center of screen
    self.up()
    
      
class Coin:
  def __init__(self):
      
      directions=["LEFT","RIGHT"] #in order to alternate sides that coins appear
      self.dire= random.choice(directions) #randomize coin location
      self.img = loadImage(path+"/images/coin.png")
      self.r=10
      self.w=50
      self.h=50
      self.y=0 - self.h
      self.music = player.loadFile(path + "/" + "coin.mp3")
            
      if self.dire == "LEFT":
        self.x=  widthtree
      else: 
        self.x = RESX - widthtree-self.w #inversing x position of coin on tree, when on right side
        
  def scoreupdate(self): #ADD MUSIC 
      if(game.racoon.contact(self)==True):
        self.music.play()  #playing coin music       
        game.score+=100 #adding 100 points to score when racoon crash into coin
        game.coin.remove(self) #removing coin from list
        
  def update(self):
      self.y += 5 #to move coins simultaneously with background, illustrate coin in static position
        
  def display(self): 
      self.scoreupdate()
      image(self.img, self.x, self.y, self.w, self.h)
      self.update()
  
class Coconut:

    def __init__(self):
        self.framenum = 1
        self.x=0
        directions=["LEFT","RIGHT"]
        self.dir= random.choice(directions) #randomizing side that coconut fall
        self.r=10
        self.w=75
        self.h=75
        self.y=0-self.h
        self.vy = 1
        self.music = player.loadFile(path + "/" + "coconut.mp3")
        self.img = []
        for i in range(5):
            coconut = loadImage(path+"/images/coconut/coconut"+ str(i) + ".png")
            self.img.append(coconut)
            
        if self.dir == "LEFT": 
            self.x= widthtree
        else: 
            self.x = RESX - widthtree - self.w
      
        
    def gravity(self): #coconut falling 
      self.vy = game.racoon.y // 1000 #increasing coconut speed as raccoon climbs higher
      self.y-=self.vy-6 
        
  
    def lifereduction(self): #music played when raccoon and coconut crashes
        self.music.pause()
        self.music.rewind()
        self.music.play()          
        game.life-=1 #removing life when raccoon and coconut crash
    
    def display(self):
      if frameCount%8 == 0:
        self.framenum = frameCount%5 #displaying different frames of coconut, illustrate coconut's motion
      
      coconutframe = self.img[self.framenum]
      
      self.gravity()
      image(coconutframe, self.x, self.y, self.w, self.h)
      
    
    def change(self):
      self.y = 0-self.h #moving coconut back up when reaches bottom or hit racoon
      directions=["LEFT","RIGHT"]
      self.dir= random.choice(directions) #randomizing coconut right or left
      if self.dir == "LEFT":
        self.x= widthtree
      else: 
        self.x = RESX - widthtree - self.w

    
    def onground(self):
      if(self.y + self.r >= RESY): #to see if coconut is out of bottom frame, reached bottom
        return True
      return False
    

class Game():
  
  def __init__(self):
    self.racoon=Racoon()
    self.score = 0
    self.life = 3
    self.coin = []
    self.play=0
    self.win=False
    self.winMusic = player.loadFile(path+"/win.mp3")
    self.bgMusic = player.loadFile(path+"/background.mp3")
    self.coco=Coconut()                    
    self.bg1=loadImage(path+"/images/trees6.png")
    self.wbg = loadImage(path+"/images/endingscreenwin.png")
    self.lbg = loadImage(path + "/images/endingscreengameover.png")
    self.bgr = 175
    self.bgb =  255
    self.bgg = 220
    self.colorbg = color(self.bgr, self.bgg, self.bgb)
    self.y_shift=0
    self.bg = []
    self.status = True

    for i in range(5): #loading background layers
        layer = loadImage(path + "/images/" + "/bgelements/" +str(i)+".png")
        self.bg.append(layer)



  def music(self): #background music to play after selection screen, stop once game lost/win
      if(self.status == True and be.play == 1):
          self.bgMusic.play()
      if(self.status == False):
          self.bgMusic.pause()
          self.bgMusic.rewind()
          
  def display(self): 
     self.music()
     
     self.colorbg = color(self.bgr, self.bgg, self.bgb) 
      
     if self.bgr >= 0: #changing bg color as racoon moves up
          self.bgr = 120 + (self.racoon.y //25)
     if self.bgg >= 0:
          self.bgg = 244 +(self.racoon.y//50)
     if self.bgb >= 25:
          self.bgb = 255 + (self.racoon.y//75)
      
        
     if(be.play!=0): 
      self.racoon.img= be.img #using racoon image as one selected in selection screen
      if (self.racoon.y % 600 == 0): #adding new coin every 600 pixels
        coin = Coin()
        self.coin.append(coin)
        

        
      if(self.life==0): #game lost screen display
        self.status = False
        image(self.lbg, 0, 0, RESX, RESY)
        textSize(30)
        fill(200,0,0)          
        text("Score: " +str(game.score), 200,50)
        text("click to restart game...", 30, RESY - 50)
        
        return
    
      if(self.racoon.y <= -15000): #game won
        self.racoon.win()
        self.winMusic.play()
        self.status = False
            

        if(self.racoon.y == -15800): #adding 1000 points once game won
            self.score += 1000
                 
        if(self.racoon.y <= -16200): #displaying win screen
            #self.score += 1000 
            edit = open("highscore.csv", "a")
            edit.write(str(self.score)+"\n")
            edit.close()
            
            image(self.wbg, 0, 0, RESX, RESY)
            textSize(30)
            fill(200,0,0)           
            text("Score: "+str(game.score),220,50)
            self.win=True
            return
    
      for i in range(3,0,-1): #parallex affect
          layershift = self.y_shift//(10*i)
          image(self.bg[i], 0, 0-layershift)
        
      for i in self.coin: #displaying coins
        i.display()
      
      
      #Image Wrap Around
      x=self.y_shift//1    
      bottom = x % RESY
      top = RESY - bottom
      image(self.bg1, 0, 0, RESX, top, 0, bottom, RESX, RESY)
      image(self.bg1, 0, top, RESX, bottom, 0, 0, RESX, bottom)
      
      layershift = self.y_shift//(1)
      image(self.bg[0], 0, 0-layershift)

      self.racoon.display()
      
      if(self.racoon.y<=RESY/(1.8)): #coconut and raccoon blinking  
        if(self.racoon.contact(self.coco)==True or self.coco.onground()==True):
            if self.racoon.contact(self.coco)== True:
                 game.racoon.blinking = True
                 game.racoon.blinkingnum = 0
                 self.coco.lifereduction()
            self.coco.change()
        
        if (self.racoon.y>-15000):
            self.coco.display()
       
       #texts during game play
      fill(200)
      textSize(15)
      text("Score: "+str(self.score), 510, 20)
      text("Life: "+str(self.life),15,20)
      fill(250)
      text("Highest Score: " + str(highscore), 250 ,20)
 
    
be=before()    
game=Game()

def setup():
    size(RESX, RESY)
  
def draw():
    background(game.colorbg)
    be.display()
    game.display()
      

    
def keyPressed():
    if(key == " "):
      game.racoon.key_handle["SPACE"] = True
      game.racoon.switch_dir()

  
def keyReleased():
    if(key == " "):
      game.racoon.key_handle["SPACE"] = False
      

      
def mouseClicked():
    global game
    global be

    if game.life == 0:
        be=before()
        game = Game()
        
        
    if game.win==True:
        be=before()
        game=Game()
    
