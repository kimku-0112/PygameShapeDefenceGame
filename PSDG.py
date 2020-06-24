import pygame, sys, random ,math , queue
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

square          = 'square'      #┐
triangle        = 'triangle'    #│ Define Shape 
pentagon        = 'pentagon'    #┘

choice_color    = cyan          #┐
BG_color        = green         #│
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
                  
tower_status    =[[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                  [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]]
                  
enemy_move      =[[60,60],[60,460]
                 ,[140,460],[140,60]
                 ,[220,60],[220,460]
                 ,[300,460],[300,60]
                 ,[380,60],[380,460]
                 ,[460,460],[460,60]
                 ,[540,60],[540,460]
                 ,[620,460],[620,60]]
                 
enemy_array     =[[1,triangle ,0,60,0,27,0],
                  [1,triangle ,0,60,0,27,0],
                  [1,triangle ,0,60,0,27,0],
                  [1,triangle ,0,60,0,27,0],
                  [1,triangle ,0,60,0,27,0],
                  [1,triangle ,0,60,0,27,0],
                  [1,triangle ,0,60,0,27,0],
                  [1,square   ,0,60,0,48,0],
                  [1,square   ,0,60,0,48,0],
                  [1,square   ,0,60,0,48,0],
                  [1,square   ,0,60,0,48,0],
                  [1,square   ,0,60,0,48,0],
                  [1,pentagon ,0,60,0,75,0],
                  [1,pentagon ,0,60,0,75,0],
                  [1,pentagon ,0,60,0,75,0]]
life_array      =[[640,480],
                  [600,480],
                  [560,480],
                  [520,480],
                  [480,480],
                  [440,480],
                  [400,480]]




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

tick_cnt = 0
time_sec = 0

life_ = 5

attack_damage = 1;
delay = 1;


def Draw_life():
    global life_
    for x in range(0,life_):
        pygame.draw.polygon(display_surf,enemy_color,((life_array[x][0] - 20    , life_array[x][1]      )\
                                                     ,(life_array[x][0]         , life_array[x][1] - 20 )\
                                                     ,(life_array[x][0] - 20    , life_array[x][1] - 40 )\
                                                     ,(life_array[x][0] - 40    , life_array[x][1] - 20 )),  2  )
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
    
def Big_Text_White(x , y , Text) :
    font = pygame.font.Font("JSDongkang-Regular.ttf", 100)
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
    Text_White(attack_up_x ,attack_up_y,"공격력(200):")
    Text_White(attack_up_x + (attack_up_width*3/4+5) ,attack_up_y,str(attack_damage))
    Text_White(delay_up_x +5   ,delay_up_y + 2 ,"타워속도(100)")
    Text_White(tower_x +5      ,tower_y + 2    ,"타워설치(100)")
    
def Make_Shape(color,shape,x,y):#x,y는 도형 중심의 좌표
    if shape == square:
        pygame.draw.rect(display_surf,color,(x -15,y-15,30,30))
    elif shape == triangle:
        pygame.draw.polygon(display_surf,color,((x,y-20),\
                                                (x+10*3*math.tan(math.radians(30)),y+10),\
                                                (x-10*3*math.tan(math.radians(30)),y+10)))
    elif shape == pentagon:
        pygame.draw.polygon(display_surf,color,((x,y - 20),\
                                                (x + 20 * math.cos(math.radians(18)),y - 20 * math.sin(math.radians(18))),\
                                                (x + 20 * math.cos(math.radians(54)),y + 20 * math.sin(math.radians(54))),\
                                                (x - 20 * math.cos(math.radians(54)),y + 20 * math.sin(math.radians(54))),\
                                                (x - 20 * math.cos(math.radians(18)),y - 20 * math.sin(math.radians(18)))))
                                                
def Enemy_move(i):#array[][0] == value //#array[][1] == shape //#array[][2] == x //#array[][3] == y //#array[][4] == cnt //#array[][5] == HP //
    global enemy_array,enemy_move,life_
    if i < 15:
        if enemy_array[i][0]:
            Make_Shape(enemy_color,enemy_array[i][1],enemy_array[i][2],enemy_array[i][3])
    
            if enemy_array[i][4] % 2 ==0:
                enemy_array[i][2]+=1
            elif enemy_array[i][4] % 4 == 1:
                enemy_array[i][3]+=1
            else :
                enemy_array[i][3]-=1
            if enemy_array[i][4]==16:
                life_ -= 1
                enemy_array[i][0] = 0
            elif enemy_array[i][2] == enemy_move[enemy_array[i][4]][0] :
                if enemy_array[i][3] == enemy_move[enemy_array[i][4]][1]:
                    enemy_array[i][4] += 1
    
    


def Time_Check():
    global tick_cnt ,time_sec
    tick_cnt += 1
    if tick_cnt == (FPS/4):
        tick_cnt = 0
        time_sec += 1
        
def Make_Enemy():
    if time_sec >= 10:
        for x in range((time_sec-10)//5):
            Enemy_move(x)
            if x <=14:
                if enemy_array[x][0]:
                    enemy_array[x][6] = 1
    else :
        Big_Text_White(300 , 240 , str(10-time_sec))

Attack_up_cost = 200
Delay_up_cost = 100
Buy_tower_cost = 100

def Attack_up():
    global attack_damage , gold
    if gold >= Attack_up_cost:
        attack_damage+=1
        gold -= Attack_up_cost
        
        
def Delay_up(m_x,m_y):
    global tower_status,gold,BG_color,Delay_up_flag
    if (tower_status[m_y][m_x] == 3)&(gold >= Delay_up_cost):
        Delay_up_flag = 0
        gold -= Delay_up_cost
        BG_color = green
        tower_status[m_y][m_x] = 4
    elif (tower_status[m_y][m_x] == 4)&(gold >= Delay_up_cost):
        Delay_up_flag = 0
        gold -= Delay_up_cost
        BG_color = green
        tower_status[m_y][m_x] = 5
    else:
        BG_color = green
        Delay_up_flag = 0
        
def Buy_tower(m_x,m_y):
    global tower_status,gold,BG_color,Delay_up_flag
    if (tower_status[m_y][m_x] == 1):
        Delay_up_flag = 0
        tower_status[m_y][m_x] = 3
        gold -= Delay_up_cost
        BG_color = green
    else:
        BG_color = green
        Delay_up_flag = 0

def Build_tower():
    global tower_status
    for y in range(0,11):
        for x in range(0,15):
            if tower_status[y][x] == 3:
                Make_Shape(tower_color,triangle,((x*40)+20),((y*40)+60))
            elif tower_status[y][x] == 4:
                Make_Shape(tower_color,square,((x*40)+20),((y*40)+60))
            elif tower_status[y][x] == 5:
                Make_Shape(tower_color,pentagon,((x*40)+20),((y*40)+60))
                
targetnum = 0
game_win_flag = 0
target_flag = 0


def Target():
    global targetnum,game_win_flag,target_flag
    target_flag = 0
    for x in range(0,15):
        if (enemy_array[x][0])&(enemy_array[x][6]):
            targetnum = x
            target_flag = 1
            break
    game_win_flag = 1;
    
def Attack(x,y):
    global enemy_array
    if math.s((enemy_array[targetnum][2] - (x+20))**2+(enemy_array[targetnum][3]-(y+20))**2)
        pygame.draw.lines(display_surf,red,False,((enemy_array[targetnum][2],enemy_array[targetnum][3]),(x+20,y+20)),10)
        enemy_array[targetnum][5] -= attack_damage   
        if enemy_array[targetnum][5] <= 0:
            enemy_array[targetnum][0] = 0

def Tri_Attack():
    for y in range(0,11):
        for x in range(0,15):
            if tower_status[y][x] == 3:
                Attack(x*40,(y+1)*40)
                
    
def Squa_Attack():
    for y in range(0,11):
        for x in range(0,15):
            if tower_status[y][x] == 4:
                Attack(x*40,(y+1)*40)
                
def Penta_Attack():
    for y in range(0,11):
        for x in range(0,15):
            if tower_status[y][x] == 5:
                Attack(x*40,(y+1)*40)
    

    


def main():
    global FPS_clock,display_surf,gold,gold_,BG_color
    gold  = 100
    gold_ = 0
    pygame.init()
    FPS_clock    = pygame.time.Clock()
    display_surf = pygame.display.set_mode((window_width,window_height ))
    pygame.display.set_caption('Shape Defence Game')
    
    Delay_up_flag = 0
    Buy_tower_flag =0
    
    mouse_x     = 0
    mouse_y     = 0
    m_x = 0
    m_y = 0
    
    while True:
        mouseClicked = False
        gold_ = gold_ + 1
        if gold_ // (FPS/2):
            gold += 10
            gold_ = 0
        
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                
                mouseClicked = True
        m_x = (mousex//40)
        if mousey<=40:
            m_y = 0
            m_x = 0
        else :
            m_y = ((mousey -40)//40)
         
        if mouseClicked:
            
            if (mousey >= shop_y) & (mousey <= (shop_y+shop_height)):
                Delay_up_flag = 0
                Buy_tower_flag = 0
                BG_color = green
                if ((mousex >= attack_up_x) & (mousex <= ((attack_up_x+attack_up_width)))):
                    Attack_up()
                elif ((mousex >= delay_up_x) & (mousex <= (delay_up_x+delay_up_width))):
                    if gold>=100:
                        Delay_up_flag = 1
                        BG_color = choice_color
                elif ((mousex >= tower_x) & (mousex <= (tower_x+tower_width))):
                    if gold>=100:
                        Buy_tower_flag = 1
                        BG_color = choice_color
            elif Delay_up_flag:
                    Buy_tower_flag = 0
                    Delay_up(m_x,m_y)
                    
            elif Buy_tower_flag:
                    Buy_tower(m_x,m_y)
            else:
                Delay_up_flag = 0
                Buy_tower_flag = 0
                BG_color = green
            

        MakeMap()
        MakeShop()
        Make_Enemy()
        Time_Check()
        Draw_life()        
        Build_tower()
        Target()
        if target_flag == 1:
            if ((tick_cnt%FPS)>=1)&((tick_cnt%FPS)<=3):
                Tri_Attack()
            if ((tick_cnt%(FPS/3*2))>=1)&((tick_cnt%(FPS/2))<=3):
                Squa_Attack()
            if ((tick_cnt%(FPS/3))>=1)&((tick_cnt%(FPS/3))<=3):
                Penta_Attack()
            
        pygame.display.update()
        FPS_clock.tick(FPS)
    
    
    
    
if __name__ == '__main__': main()











































