import pygame,sys
import pygame.locals
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    K_s,
    QUIT,
)
pygame.init()
visited=[]
stack=[]
#computer
class Computer():
    def __init__(self):
        self.x = 100
        self.y = 50
        self.speed = 25
        
    def move(self):
        #print(stack)
        move_x=self.x + self.speed
        move_y=self.y
        if (move_x,move_y)  in  walls or (move_x,move_y) in stack:
            move_x=self.x 
            move_y=self.y + self.speed
            if (move_x,move_y)  in  walls or (move_x,move_y) in stack:
                move_x=self.x - self.speed
                move_y=self.y 
                if (move_x,move_y)  in  walls or (move_x,move_y) in stack:
                    move_x=self.x - self.speed
                    move_y=self.y 
                    if (move_x,move_y)  in  walls or (move_x,move_y) in stack:    
                        stack.pop()
                        walls.append((self.x,self.y))
                        self.move()
                       
                    else:
                        
                        stack.append((self.x,self.y))
                        self.y =self.y - self.speed      
                else:
                    stack.append((self.x,self.y)) 
                    self.x =self.x - self.speed 
                           
            else:
                stack.append((self.x,self.y))
                self.y =self.y + self.speed       
        else:
            stack.append((move_x,move_y))
            self.x =self.x + self.speed

<<<<<<< HEAD:finalmaze.py
        if(self.x,self.y) in treasures:
                    print("computer win!")
                    computer_end()    
          
=======
stack=[]
#computer
class Computer():
    def __init__(self):
        self.x = 100
        self.y = 50
        self.speed = 25
        
    def move(self):
        #print(stack)
        move_x=self.x + self.speed
        move_y=self.y
        if (move_x,move_y)  in  walls or (move_x,move_y) in stack:
            move_x=self.x 
            move_y=self.y + self.speed
            if (move_x,move_y)  in  walls or (move_x,move_y) in stack:
                move_x=self.x - self.speed
                move_y=self.y 
                if (move_x,move_y)  in  walls or (move_x,move_y) in stack:
                    move_x=self.x - self.speed
                    move_y=self.y 
                    if (move_x,move_y)  in  walls or (move_x,move_y) in stack:    
                        x=stack.pop(-1)
                        print(x)
                        stack.append((self.x,self.y))
                        print(stack)
                    else:
                        stack.append((self.x,self.y))
                        self.y =self.y - self.speed        
                else:
                    stack.append((self.x,self.y)) 
                    self.x =self.x - self.speed        
            else:
                stack.append((self.x,self.y))
                self.y =self.y + self.speed       
        else:
            stack.append((move_x,move_y))
            self.x =self.x + self.speed
        if(self.x,self.y) in treasures:
                    print("computer win!")
                    computer_end()    
        

        

        
    
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
#player
class Player():
    
    def __init__(self):
        self.x = 100
        self.y = 50
        self.speed = 25

    
    def move(self,pressed_key):

        if (pressed_key[K_LEFT]):
            move_to_x=self.x - self.speed
            move_to_y=self.y
            if(move_to_x,move_to_y) not in  walls:
                self.x =self.x - self.speed
<<<<<<< HEAD:finalmaze.py
              
=======
            if(self.x,self.y) in treasures:
                    print("you win!")
                    player_end()        
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
            

        if (pressed_key[K_RIGHT]):
            move_to_x=self.x + self.speed
            move_to_y=self.y
            #print(move_to_x,move_to_y)
            if(move_to_x,move_to_y) not in  walls:
                self.x =self.x + self.speed
<<<<<<< HEAD:finalmaze.py
            

=======
            if(self.x,self.y) in treasures:
                    print("you win!")
                    player_end()        


>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
        if (pressed_key[K_UP]):
            move_to_x=self.x 
            move_to_y=self.y - self.speed
            if(move_to_x,move_to_y) not in  walls :
                self.y =self.y - self.speed
<<<<<<< HEAD:finalmaze.py
            
=======
            if(self.x,self.y) in treasures:
                    print("you win!")
                    player_end()        

>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
                
                    
        if (pressed_key[K_DOWN]):
            move_to_x=self.x 
            move_to_y=self.y + self.speed
            if(move_to_x,move_to_y) not in  walls:
                self.y=self.y + self.speed
<<<<<<< HEAD:finalmaze.py

        if(self.x,self.y) in treasures:
            print("you win!")
            player_end()        

=======
            if(self.x,self.y) in treasures:
                    print("you win!")
                    player_end()        

>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py

        
#treasures
class Treasure:
    def __init__(self):
        self.x=600
        self.y=600
      

#board
walls = []
treasures = []
levels= [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXP  XXXXXXX          XXXXX",
"XXX   XXXXXXX  XXXXXX  XXXXX",
"XXX       XX  XXXXXXX  XXXXX",
"XXXX      XX  XXX         XX",
"XXXXXXXX  XX  XXX         XX",
"XXXXXXXX  XX  XXXXXX   XXXXX",
"XXXXXXXX  XX    XXXX   XXXXX",
"XX    XXX                  X",
<<<<<<< HEAD:finalmaze.py
"XX    XXXXXXXXXXX  XXXXXXXXX",
"XXX        XXXXXX   XX   XXX",
"XXX                XX  XXXXX",
"XXXXXXXXXXXXXXX    XX XXX  X",
"XXXXXXXXX    XXX   XXXXX   X",
=======
"XX    XXXXXXXXXXXXXXXXXXXX X",
"XXX        XXXXXXXXXXXXXXX X",
"XXX                XXXXXXX X",
"XXXXXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXXX    XXXXX  X",
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
"XXXX   XXXXXXXXXXX         X",
"XXXXX                      X",
"XXXXX          XXXXXXXXXXX X",
"XXXXXXXXXXX    XXXXXXXXXXX X",
"XXXXXXXXXXXX               X",
"X     XXX        XXXXXX    X",
"X     XXX        XXXXXX    X",
"XXX   XXXXXXX              X",
"XXX   XXXXXXXXXXXXXX   XXXXX",
<<<<<<< HEAD:finalmaze.py
"XXX   YXXXXXXXX  XXX   XXXXX",
"XXX          XX  XX     TXXX",
=======
"XXX   YXXXXXXXXXXXXX   XXXXX",
"XXX          XXXXXX     TXXX",
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
"XXX          XXXXXX      XXX",
"XXXXXXXXXXX          XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

def blocks(levels):
    for i in range(len(levels)):
        for j in range(len(levels[i])):
            if levels[j][i] == "X":
                walls.append((i*25,j*25))
            if levels[j][i] == "T":           
                treasures.append((i*25,j*25))
                print(treasures)

def Board(levels):
    num = 800//32
    for i in range(len(levels)):
        for j in range(len(levels[i])):
            if levels[j][i] == "X":
                #pygame.draw.rect(screen,"gray",((i*num),(j*num),25,25))
                size = pygame.transform.scale(img_blocks,(25,25))
                screen.blit(size,(i*num,j*num))  


#sounds
pygame.mixer.init()
#music_bg = pygame.mixer.music.load(("bg.ogg"))
#pygame.mixer.music.paly(music_bg )                

#timeer
clock = pygame.time.Clock()
start = 0           

#text
def draw_text(text,font,text_color,x,y):
    img = font.render(text,True,text_color)
    screen.blit(img,(x,y))              
                
def player_end():
    global end1
    player.x=100
    player.y=50
    end1 = True

def computer_end():
    global end2
    computer.x=100
    computer.y=50
    end2 = True

#img_treasure = pygame.image.load("ball.jpg")
img_player = pygame.image.load("pingi.jpg")
img_bg = pygame.image.load("texture-surface-dark-blue-11570456514lgg3xugs36.jpg")   
img_blocks = pygame.image.load("icy_block.png")   

#background
def background(img_bg):
    size = pygame.transform.scale(img_bg,(700,700))
    screen.blit(size,(0,0)) 
                 
screen = pygame.display.set_mode((700,700))
font = pygame.font.SysFont("arialblack",30)
font2 =  pygame.font.SysFont("arialblack",20)
TEXT_COLOR = ("black")
pygame.display.set_caption("MAZE")
player = Player()
computer=Computer()
treasure = Treasure()
blocks(levels)
end1 = False
end2 = False
#print(walls)


#main game
running = True
while running:
    pygame.time.delay(120)
    
    for event in pygame.event.get():
       
        if event.type == KEYDOWN:
           
            if event.key == K_ESCAPE:
               running = False

<<<<<<< HEAD:finalmaze.py
            if event.key == K_SPACE and end1==True or end2 == True:
                end1 = False
                end2 = False
=======
            if event.key == K_SPACE and end1==True or end2 == False:
                end1 = False
                end2 =False
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
                start = 0
                
                
        elif event.type == pygame.locals.QUIT:
            running == False 
            pygame.quit()
            sys.exit()
    pressed_key = pygame.key.get_pressed()
    player.move(pressed_key)
    computer.move()
    screen.fill((0,0,0))
    background(img_bg)
    Board(levels)
    pygame.draw.circle(screen,"gold",(treasure.x+12.5,treasure.y+12.5),12.5)
    pygame.draw.rect(screen,"red",(computer.x,computer.y,25,25))   
    size = pygame.transform.scale(img_player,(25,25))
    screen.blit(size,(player.x,player.y))
    #size2 = pygame.transform.scale(img_treasure,(25,25))
    #screen.blit(size2,(treasure.x+12.5,treasure.y+12.5))
<<<<<<< HEAD:finalmaze.py
    if end1 == False and end2 == False:
=======
    if end1 == False or end2 == False:
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
        start +=1     
    
    if end1==True:
        time = start
        end1=True
<<<<<<< HEAD:finalmaze.py
        pygame.draw.rect(screen,"gold",(0,0,700,700))
=======
        pygame.draw.rect(screen,"gold",(100,230,500,200))
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
        draw_text(f"you win!",font,TEXT_COLOR,170,260)
        draw_text(f"total time: {time}ms",font,"blue",170,310)
        draw_text("press SPACE to restart",font,TEXT_COLOR,170,360)
    if end2==True:
        time = start
<<<<<<< HEAD:finalmaze.py
        stack = []
        end2=True
        pygame.draw.rect(screen,"red",(0,0,700,700))
=======
        end2=True
        pygame.draw.rect(screen,"red",(100,230,500,200))
>>>>>>> 4c4d0d1dfddae81e9ff89534cc67e58e8cf09513:maze4.py
        draw_text(f"computer win!",font,TEXT_COLOR,170,260)
        draw_text(f"total time: {time}ms",font,"blue",170,310)
        draw_text("press SPACE to restart",font,TEXT_COLOR,170,360)
    pygame.draw.rect(screen,"gold",(580,10,100,50))
    draw_text(f'time:{start}' ,font2,TEXT_COLOR,580,20)    
     
    pygame.display.update()
       
pygame.quit()
