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

Attack_up_cost  = 200
Delay_up_cost   = 100
Buy_tower_cost  = 100
targetnum       = 0
win_flag        = 0
lose_flag       = 0
target_flag     = 0
Delay_up_flag   = 0
Buy_tower_flag  = 0
Hard_Mode_flag  = 0


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
                 
E_enemy_array   =[[1,triangle ,0,60,0,81,0,100],
                  [1,triangle ,0,60,0,81,0,100],
                  [1,triangle ,0,60,0,81,0,100],
                  [1,triangle ,0,60,0,81,0,100],
                  [1,triangle ,0,60,0,81,0,100],
                  [1,triangle ,0,60,0,81,0,100],
                  [1,triangle ,0,60,0,81,0,100],
                  [1,square   ,0,60,0,192,0,200],
                  [1,square   ,0,60,0,192,0,200],
                  [1,square   ,0,60,0,192,0,200],
                  [1,square   ,0,60,0,192,0,200],
                  [1,square   ,0,60,0,192,0,200],
                  [1,pentagon ,0,60,0,375,0,300],
                  [1,pentagon ,0,60,0,375,0,300],
                  [1,pentagon ,0,60,0,375,0,300]]
E_enemy_unit = 15
                  
H_enemy_array     =[[1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,triangle ,0,60,0,243,0,50],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,square   ,0,60,0,768,0,70],
                    [1,pentagon ,0,60,0,1875,0,100],
                    [1,pentagon ,0,60,0,1875,0,100],
                    [1,pentagon ,0,60,0,1875,0,100],
                    [1,pentagon ,0,60,0,1875,0,100],
                    [1,pentagon ,0,60,0,1875,0,100],
                    [1,pentagon ,0,60,0,1875,0,100]]
H_enemy_unit = 30
life_array      =[[640,480],
                  [600,480],
                  [560,480],
                  [520,480],
                  [480,480],
                  [440,480],
                  [400,480]]


enemy_unit      = E_enemy_unit
enemy_array     = E_enemy_array
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

attack_damage = 1


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
    font = pygame.font.Font("./font/JSDongkang-Regular.ttf", 20)
    text = font.render(Text,True,(255,255,255))
    textrect = text.get_rect()
    textrect.topleft = [x , y]
    display_surf.blit(text, textrect)
    
def Big_Text_White(x , y , Text) :
    font = pygame.font.Font("./font/JSDongkang-Regular.ttf", 70)
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
    if i < enemy_unit:
        if enemy_array[i][0]:
            Make_Shape(enemy_color,enemy_array[i][1],enemy_array[i][2],enemy_array[i][3])
    
            if enemy_array[i][4] % 2 ==0:
                enemy_array[i][2]+=(60/FPS)
            elif enemy_array[i][4] % 4 == 1:
                enemy_array[i][3]+=(60/FPS)
            else :
                enemy_array[i][3]-=(60/FPS)
            if enemy_array[i][4]==16:
                life_ -= 1
                enemy_array[i][0] = 0
            elif enemy_array[i][2] == enemy_move[enemy_array[i][4]][0] :
                if enemy_array[i][3] == enemy_move[enemy_array[i][4]][1]:
                    enemy_array[i][4] += 1
    
    


def Time_Check():
    global tick_cnt ,time_sec
    tick_cnt += 1
    if tick_cnt == (FPS):
        tick_cnt = 0
        time_sec += 1
        
def Make_Enemy():
    if time_sec >= 10:
        for x in range((time_sec-10)//3):
            Enemy_move(x)
            if x < enemy_unit:
                if enemy_array[x][0]:
                    enemy_array[x][6] = 1
    else :
        Big_Text_White(300 , 240 , str(10-time_sec))

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
    global tower_status,gold,BG_color,Buy_tower_flag
    if (tower_status[m_y][m_x] == 1)&(gold>=100):
        tower_status[m_y][m_x] = 3
        gold -= Delay_up_cost
        BG_color = green
        buildsound.play()
        Buy_tower_flag = 0
    else:
        BG_color = green
        Buy_tower_flag = 0

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
                
def Target():
    global targetnum,win_flag,target_flag
    target_flag = 0
    for x in range(0,enemy_unit):
        if (enemy_array[x][0]):
            if(enemy_array[x][6]):
                targetnum = x
                target_flag = 1
                break
        else :
            if x == (enemy_unit-1):
                win_flag = 1;
    
def Attack(x,y):
    global enemy_array,gold
    if math.sqrt((enemy_array[targetnum][2] - (x+20))**2+(enemy_array[targetnum][3]-(y+20))**2) <= 300:
        pygame.draw.lines(display_surf,red,False,((enemy_array[targetnum][2],enemy_array[targetnum][3]),(x+20,y+20)),10)
        enemy_array[targetnum][5] -= attack_damage   
        if enemy_array[targetnum][5] <= 0:
            enemy_array[targetnum][0] = 0
            goldsound.play()
            gold += enemy_array[targetnum][7]

def Tri_Attack():
    for y in range(0,11):
        for x in range(0,15):
            if tower_status[y][x] == 3:
                if ((tick_cnt%FPS)==1):
                    shotsound.play()
                Attack(x*40,(y+1)*40)
                
    
def Squa_Attack():
    for y in range(0,11):
        for x in range(0,15):
            if tower_status[y][x] == 4:
                if ((tick_cnt%(FPS/3*2))==1):
                    shotsound.play()
                Attack(x*40,(y+1)*40)
                
def Penta_Attack():
    for y in range(0,11):
        for x in range(0,15):
            if tower_status[y][x] == 5:
                if ((tick_cnt%(FPS/3))==1):
                    shotsound.play()
                Attack(x*40,(y+1)*40)
    

    


def main():
    global FPS_clock,display_surf,gold,gold_,BG_color,lose_flag,win_flag,Hard_Mode_flag,\
           Delay_up_flag,Buy_tower_flag,enemy_array,life_,time_sec,enemy_unit,attack_damage,tower_status,\
           shotsound,goldsound,winsound,losesound,buildsound
    gold  = 0
    gold_ = 0
    pygame.init()
    FPS_clock    = pygame.time.Clock()
    display_surf = pygame.display.set_mode((window_width,window_height ))
    pygame.display.set_caption('Shape Defence Game')
    pygame.mixer.init()
    
    pygame.mixer.music.load("./audio/BGM1_.mp3")         #BGM
    shotsound   = pygame.mixer.Sound("./audio/S_shot.wav")
    goldsound   = pygame.mixer.Sound("./audio/S_gold.wav")
    winsound    = pygame.mixer.Sound("./audio/S_win.wav")
    losesound   = pygame.mixer.Sound("./audio/S_lose.wav")
    buildsound  = pygame.mixer.Sound("./audio/S_buld.wav")
    
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    
    mousex     = 0
    mousey     = 0
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
                Delay_up_flag = 0
                Buy_tower(m_x,m_y)
            else:
                Delay_up_flag = 0
                Buy_tower_flag = 0
                BG_color = green
        if life_ <= 0:
            lose_flag = 1;
        if (win_flag == 0) & (lose_flag == 0):
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
        elif win_flag == 1:
            winsound.play()
            display_surf.fill(blue)
            Big_Text_White(160,200,"YOU WIN!!")
            if Hard_Mode_flag == 0:
                Text_White(240,300,"Hard Mode?")
                pygame.draw.rect(display_surf,shop_color,(235,290,140,30),2)
                if (mouseClicked):
                    if (mousex >= 240)&(mousex <= 440):
                        if (mousey>=300)&(mousey<=320):
                            win_flag = 0;
                            Hard_Mode_flag = 1
                            enemy_array = H_enemy_array
                            life_ = 3
                            attack_damage = 1
                            time_sec = 0
                            gold = 0
                            enemy_unit      = H_enemy_unit
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
            else:
                if mouseClicked:
                    pygame.quit()
                    sys.exit()
        elif lose_flag == 1:
            losesound.play()
            display_surf.fill(red)
            Big_Text_White(140,200,"YOU LOSE!!")
            if mouseClicked:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        FPS_clock.tick(FPS)
    
    
    
    
if __name__ == '__main__': main()











































