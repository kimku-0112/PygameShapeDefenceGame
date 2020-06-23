import pygame, sys, random
from pygame.locals import *

FPS             = 60           #┐
window_width    = 640          #│
window_height   = 480          #│ Define System Information 
reveal_speed    = 8            #│ 
gap_size        = 0            #│
box_size        = 40           #┘

gray            = (100,100,100)     #┐
navyblue        = (60,60,100)       #│
white           = (255,255,255)     #│
red             = (255,0,0)         #│
green           = (0,255,0)         #│ Define Color
blue            = (0,0,255)         #│
yellow          = (255,200,0)       #│
orange          = (255,128,0)       #│
purple          = (255,0,255)       #│
cyan            = (0,255,255)       #┘

mapcolor        =[[1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                  [0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1]]
                  
enemy_move      =[[20,60]
                 ,[60,60],[60,460]
                 ,[140,460],[140,60]
                 ,[220,60],[220,460]
                 ,[300,460],[300,60]
                 ,[380,60],[380,460]
                 ,[460,460],[460,60]
                 ,[540,60],[540,460]
                 ,[620,460],[620,60]]

BG_color        = green         #┐
light_color     = gray          #│ System Color
box_color       = white         #│
highlight_color = blue          #┘
tower_color     = gray          #┐
enemy_color     = red           #│
road_color      = gray          #│
shop_color      = white         #│
gold_color      = yellow        #│ Object Color
attack_up_color = red           #│
s_tower_color   = green         #│
delay_up_color  = blue          #┘

square          = 'square'      #┐
triangle        = 'triangle'    #│ Define Shape 
pentagon        = 'pentagon'    #┘

map_width       = int(window_width  / box_size)
map_heghit      = int(window_height / box_size)-1
shop_x          = 0
shop_y          = 0
shop_width      = window_width
shop_height     = window_height - (map_heghit * box_size)
attack_up_x     = shop_x + 10
attack_up_y     = shop_y + 5
attack_up_width = int(shop_width / 4) - 20
attack_up_height= shop_height - 10
delay_up_x      = attack_up_x + attack_up_width + 20
delay_up_y      = shop_y + 5
delay_up_width  = int(shop_width / 4) - 20
delay_up_height = shop_height - 10
tower_x         = delay_up_x + delay_up_width + 20
tower_y         = shop_y + 5
tower_width     = int(shop_width / 4) - 20
tower_heghit    = shop_height - 10
gold_x          = tower_x + tower_width + 20
gold_y          = shop_y + 5
gold_width      = int(shop_width / 4) - 20
gold_height     = shop_height - 10

def GetBoxAtPixel(x, y):
    for boxx in range(map_width):
        for boxy in range(map_heghit):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, box_size, box_size)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)
    
def MakeMap():
    
    for x in range(0,map_width):
        for y in range(0,map_heghit):
            if mapcolor[y][x] : pygame.draw.rect(display_surf,road_color,(x * box_size,(y+1) * box_size,box_size,box_size))
            else :              pygame.draw.rect(display_surf,BG_color  ,(x * box_size,(y+1) * box_size,box_size,box_size))
    
def Text_White(x , y , Text) :
    font = pygame.font.Font("JSDongkang-Regular.ttf", 20)
    text = font.render(Text,True,(255,255,255))
    textrect = text.get_rect()
    textrect.topleft = [x , y]
    display_surf.blit(text, textrect)
    
def MakeShop():
    pygame.draw.rect(display_surf,shop_color        ,(shop_x,shop_y,shop_width,shop_height))
    pygame.draw.rect(display_surf,delay_up_color    ,(attack_up_x,attack_up_y,attack_up_width,attack_up_height))
    pygame.draw.rect(display_surf,attack_up_color   ,(delay_up_x,delay_up_y,delay_up_width,delay_up_height))
    pygame.draw.rect(display_surf,s_tower_color     ,(tower_x,tower_y,tower_width,tower_heghit))
    pygame.draw.rect(display_surf,gold_color        ,(gold_x,gold_y,gold_width,gold_height))
    Text_White(gold_x + 20      , gold_y + 5    , str(gold))
    Text_White(attack_up_x + 40 ,attack_up_y + 2,"공격력")
    Text_White(delay_up_x +30   ,delay_up_y + 2 ,"공격속도")
    Text_White(tower_x +30      ,tower_y + 2    ,"타워 구매")
def Make_Shape(shape,x,y):#x,y는 중심에서의 좌표
    
def Enemy_move(shape):
    if shape == 'square':
        
    elif shape == 'triangle':
        
    elif shape == 'pentagon':
        
    
    


def main():
    global FPS_clock,display_surf,gold,gold_
    gold  = 0
    gold_ = 0
    pygame.init()
    FPS_clock    = pygame.time.Clock()
    display_surf = pygame.display.set_mode((window_width,window_height ))
    pygame.display.set_caption('Shape Defence Game')
    
    
    
    mouse_x     = 0
    mouse_y     = 0
    
    while True:
        gold_ = gold_ + 1
        if gold_ // 30:
            gold += 10
            gold_ = 0
        
        
        MakeMap()
        MakeShop()
        
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            #elif event.type == KEYDOWN:
            #   if event.key == pygame.K_ESCAPE:
            #elif event.type == KEYUP:

        

                
    
        pygame.display.update()
        FPS_clock.tick(FPS)
    
    
    
    
if __name__ == '__main__': main()











































