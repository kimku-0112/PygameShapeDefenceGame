<<<<<<< HEAD
=======


>>>>>>> d04c18293fb0b3a3ccf31730888844657ca8254e
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
yellow          = (255,255,0)       #│
orange          = (255,128,0)       #│
purple          = (255,0,255)       #┘
cyan            = (0,255,255)       

BG_color        = green         #┐
light_color     = gray          #│ System Color
box_color       = white         #│
highlight_color = blue          #┘
tower_color     = red           #┐
enemy_color     = gray          #│
road_color      = gray          #│
shop_color      = white         #│ Object Color
gold_color      = yellow        #│
attack_up_color = red           #│
delay_up_color  = blue          #┘

square          = 'square'      #┐
triangle        = 'triangle'    #│ Define Shape 
pentagon        = 'pentagon'    #┘

map_width       = int(window_width  / box_size)-1
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
none_x          = delay_up_x + delay_up_width + 20
none_y          = shop_y + 5
none_width      = int(shop_width / 4) - 20
none_heghit     = shop_height - 10
gold_x          = none_x + none_width + 20
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
    display_surf.fill(BG_color)
    
    
def MakeShop():
    pygame.draw.rect(display_surf,shop_color        ,(shop_x,shop_y,shop_width,shop_height))
    pygame.draw.rect(display_surf,delay_up_color    ,(attack_up_x,attack_up_y,attack_up_width,attack_up_height))
    pygame.draw.rect(display_surf,attack_up_color   ,(delay_up_x,delay_up_y,delay_up_width,delay_up_height))
    pygame.draw.rect(display_surf,shop_color        ,(none_x,none_y,none_width,none_heghit))
    pygame.draw.rect(display_surf,gold_color        ,(gold_x,gold_y,gold_width,gold_height))


def main():
    global FPS_clock,display_surf
    pygame.init()
    FPS_clock    = pygame.time.Clock()
    display_surf = pygame.display.set_mode((window_width,window_height ))
    pygame.display.set_caption('Shape Defence Game')
    font = pygame.font.Font('새굴림', 32)
    text = font.renser("
    
    mouse_x     = 0
    mouse_y     = 0
    
    while True:
        MakeMap()
        MakeShop()
    
        pygame.display.update()
        FPS_clock.tick(FPS)
    
    
    
    
if __name__ == '__main__': main()











































