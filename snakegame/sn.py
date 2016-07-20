import pygame
import time
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(85,107,47)
blue=(25,25,112)
blue2=(0,178,238)
blue3=(202,255,255)
purple1=(171,130,255)
display_width=800
display_height=400
FPS=15
direction="right"

#pygame.display.flip()
soundObj = pygame.mixer.Sound('sound1.wav')
pygame.display.set_caption('Bizzard')
icon=pygame.image.load('snakehead2.png')
cobra=pygame.image.load('cobra.gif')
background=pygame.image.load('1.jpg')
#backgroundRect=background.get_rect()
#size=(width,height)=background.get_size()
gameDisplay=pygame.display.set_mode((display_width,display_height))
#gameDisplay.(background,[0,0])
pygame.display.set_icon(icon) 
img=pygame.image.load('snakehead1.png')
frog=pygame.image.load('rat.png')
rat=pygame.image.load('frog.png')
#pygame.display.update()

clock=pygame.time.Clock()
block_size=20
AppleThickness=60
RatThickness=60
smallfont=pygame.font.SysFont("comicsansms",25)
mediumfont=pygame.font.Font("Gagalin-Regular.otf",30)
mediumfont1=pygame.font.Font("Gagalin-Regular.otf",50)
largefont=pygame.font.Font("Xacto Blade.ttf",80)
extralarge=pygame.font.Font("Xacto Blade.ttf",120)
def pause():
       paused=True
       message_to_screen("Paused",blue2,-100,size="large")
       message_to_screen("Press C to continue and Q to quit",black,25)
       pygame.display.update()
       while paused:
              for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_c:
                            paused=False
                     elif event.key==pygame.K_q:
                            pygame.quit()
                            quit()
              #gameDisplay.fill(white)
              
              clock.tick(5)
def score(score):
       text=mediumfont1.render("Score:"+str(score),True,white)
       gameDisplay.blit(text,[320,0])
def randratGen():
       randratX=round(random.randrange(0,display_width-RatThickness-20))
       randratY=round(random.randrange(0,display_width-RatThickness-20))
       return randratX,randratY
def randAppleGen():
       randAppleX=round(random.randrange(0,display_width-AppleThickness))#/20.0)*20.0
       randAppleY=round(random.randrange(0,display_height-AppleThickness))#/20.0)*20.0
       return randAppleX,randAppleY
def game_intro():
       intro=True

       while intro:
              for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       pygame.quit()
                       quit()
                       
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key==pygame.K_c:
                        intro=False
              gameDisplay.fill(white)
              gameDisplay.blit(cobra,[0,150])
             
              message_to_screen("Welcome to Bizzard",green,-100,"large")
              message_to_screen("Eat as many as you can ...frogs and rats are soo tasty:)",blue,-30,"medium" )
              message_to_screen("Press C to play and Q to quit",red,10,"small")
              pygame.display.update()
              
              clock.tick(15)
def snake(block_size,snakeList):
       if direction=="right":
           head=img
       if direction=="left":
           head=pygame.transform.rotate(img,180)
       if direction=="up":
           head=pygame.transform.rotate(img,90)
       if direction=="down":
           head=pygame.transform.rotate(img,270)
       gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
       for XnY in snakeList[:-1]:
           pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
def text_objects(text,color,size):
    if size=="small":
       textSurface=smallfont.render(text,True,color)
    elif size=="medium":
       textSurface=mediumfont.render(text,True,color)
    elif size=="large":
       textSurface=largefont.render(text,True,color)
    elif size=="extralarge":
       textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()
def message_to_screen(msg,color,y_displace=0,size="small"):
     textSurface,textRect=text_objects(msg,color,size)
    #screen_text=font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])
     textRect.center=(display_width/2),(display_height/2)+y_displace
     gameDisplay.blit(textSurface,textRect)
def gameLoop():
    global direction
    direction="right"
    gameExit=False
    gameOver=False
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=10
    lead_y_change=0
    snakeList=[]
    snakeLength=1
    randratX,randratY=randratGen()
    randAppleX,randAppleY=randAppleGen()
   
    while not gameExit:
       if gameOver==True:
            message_to_screen("Game over",purple1,y_displace=-50,size="extralarge")
            message_to_screen("Press C to play again and Q to quit",blue3,50,size="medium")
            pygame.display.update()
       while gameOver==True:
            #gameDisplay.fill(white)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       gameOver=False
                       gameExit=True
                       
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
    

        
       for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    direction="up"
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    direction="down"   
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key==pygame.K_p:
                    pause()
                     
            if(lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0):
               gameOver=True
       lead_x+=lead_x_change
       lead_y+=lead_y_change
       gameDisplay.blit(background,[0,0])
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
       gameDisplay.blit(frog,(randAppleX,randAppleY))
       gameDisplay.blit(rat,(randratX,randratY))
       snakeHead=[]
       snakeHead.append(lead_x)
       snakeHead.append(lead_y)
       snakeList.append(snakeHead)
       if len(snakeList)>snakeLength:
            del snakeList[0]
       for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
       snake(block_size,snakeList)
       score(snakeLength-1)
       pygame.display.update()
        #if lead_x==randAppleX and lead_y==randAppleY:
             #randAppleX=round(random.randrange(0,display_width-block_size)/20.0)*20.0
             #randAppleY=round(random.randrange(0,display_height-block_size)/20.0)*20.0
             #snakeLength+=1
##        if lead_x>=randAppleX and lead_x<=randAppleX+AppleThickness:
##            if lead_y>=randAppleY and lead_y<=randAppleY+AppleThickness:
##              randAppleX=round(random.randrange(0,display_width-block_size)/20.0)*20.0
##              randAppleY=round(random.randrange(0,display_height-block_size)/20.0)*20.0
##              snakeLength+=1
       if lead_x > randAppleX and lead_x < randAppleX+AppleThickness or lead_x+block_size>randAppleX and lead_x+block_size<randAppleX+AppleThickness:
               if lead_y>randAppleY and lead_y<randAppleY+AppleThickness or lead_y+block_size>randAppleY and lead_y+block_size<randAppleY+AppleThickness:
                      print ("X and Y crossover")
                      
                  # wait and let the sound play for 1 second
                    
                      randAppleX,randAppleY=randAppleGen()
                      snakeLength+=1
       
       elif lead_x > randratX and lead_x < randratX+RatThickness or lead_x+block_size>randratX and lead_x+block_size<randratX+RatThickness:
               if lead_y>randratY and lead_y<randratY+RatThickness or lead_y+block_size>randratY and lead_y+block_size<randratY+RatThickness:
                      print ("X and Y crossover")
                      
                      # wait and let the sound play for 1 second
                     
                      randratX,randratY=randratGen()
                      snakeLength+=5
              
       clock.tick(FPS)

         
  
    pygame.quit()
    quit()
game_intro()
gameLoop()
