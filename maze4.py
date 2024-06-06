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

#player
class Player():
    
    def __init__(self):
        self.x = 100
        self.y = 50
        self.speed = 25

    
    def move(self,pressed_key):

        if (pressed_key[pygame.K_LEFT]):
            move_to_x=self.x - self.speed
            move_to_y=self.y
            if(move_to_x,move_to_y) not in  walls:
                self.x =self.x - self.speed
                if(self.x,self.y) in treasures:
                    print("you win!")
                    game_end()
            

        if (pressed_key[pygame.K_RIGHT]):
            move_to_x=self.x + self.speed
            move_to_y=self.y
            #print(move_to_x,move_to_y)
            if(move_to_x,move_to_y) not in  walls:
                self.x =self.x + self.speed
                if(self.x,self.y) in treasures:
                    print("you win!")
                    game_end()

        if (pressed_key[pygame.K_UP]):
            move_to_x=self.x 
            move_to_y=self.y - self.speed
            if(move_to_x,move_to_y) not in  walls:
                self.y =self.y - self.speed
                if(self.x,self.y) in treasures:
                    print("you win!")
                    game_end()
                    
        if (pressed_key[pygame.K_DOWN]):
            move_to_x=self.x 
            move_to_y=self.y + self.speed
            if(move_to_x,move_to_y) not in  walls:
                self.y  =self.y + self.speed
                if(self.x,self.y) in treasures:
                    print("you win!")
                    game_end()

#treasures
class Treasure:
    def __init__(self):
        self.x=500
        self.y=200 

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
"XX    XXX        XXXT  XXXXX",
"XX    XXX  XXXXXXXXXXXXXXXXX",
"XXX        XXXXXXXXXXXXXXXXX",
"XXX                XXXXXXXXX",
"XXXXXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXXX    XXXXX  X",
"XXXX   XXXXXXXXXXX        XX",
"XXXXX                     XX",
"XXXXX          XXXXXXXXXXXXX",
"XXXXXXXXXXX    XXXXXXXXXXXXX",
"XXXXXXXXXXXX               X",
"X     XXX        XXXXXX    X",
"X     XXX        XXXXXX    X",
"XXX   XXXXXXX              X",
"XXX   XXXXXXXXXXXXXX   XXXXX",
"XXX   YXXXXXXXXXXXXX   XXXXX",
"XXX          XXXXXX      XXX",
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
                
def game_end():
    global end
    player.x=100
    player.y=50
    end = True

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
treasure = Treasure()
blocks(levels)
end = False
#print(walls)


#main game
running = True
while running:
    pygame.time.delay(120)
    
    for event in pygame.event.get():
       
        if event.type == KEYDOWN:
           
            if event.key == K_ESCAPE:
               running = False

            if event.key == K_SPACE and end==True:
                end = False
                
        elif event.type == pygame.locals.QUIT:
            running == False 
            pygame.quit()
            sys.exit()
    pressed_key = pygame.key.get_pressed()
    player.move(pressed_key)
    screen.fill((0,0,0))
    background(img_bg)
    Board(levels)
    pygame.draw.circle(screen,"gold",(treasure.x+12.5,treasure.y+12.5),12.5)
    #pygame.draw.rect(screen,"red",(player.x,player.y,25,25))   
    size = pygame.transform.scale(img_player,(25,25))
    screen.blit(size,(player.x,player.y))
    #size2 = pygame.transform.scale(img_treasure,(25,25))
    #screen.blit(size2,(treasure.x+12.5,treasure.y+12.5))  
    if end==True:
        time = start
        start = 0
        pygame.draw.rect(screen,"gold",(100,230,500,200))
        draw_text(f"you win! time:{time}",font,TEXT_COLOR,200,260)
        draw_text("press SPACE to restart",font,TEXT_COLOR,170,340)
    pygame.draw.rect(screen,"gold",(580,10,100,50))
    draw_text(f'time: {start}' ,font2,TEXT_COLOR,590,20)    
    start +=1    
    pygame.display.update()
       
pygame.quit()