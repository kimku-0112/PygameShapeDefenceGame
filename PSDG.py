import pygame, sys, random
from pygame.locals import *

FPS             = 60            #┐
WINDOWWIDTH     = 640           #│Define System Information 
WINDOWHEIGHT    = 480           #┘

GRAY        = (100,100,100)     #┐
NAVYBLUE    = (60,60,100)       #│
WHITE       = (255,255,255)     #│
RED         = (255,0,0)         #│
GREEN       = (0,255,0)         #│ Define Color
BLUE        = (0,0,255)         #│
YELLOW      = (255,255,0)       #│
ORANGE      = (255,128,0)       #│
PURPLE      = (255,0,255)       #┘
CYAN        = (0,255,255)       

BGCOLOR         = NAVYBLUE      #┐
LIGHTBGCOLOR    = GRAY          #│ System Color
BOXCOLOR        = WHITE         #│
HIGHLIGHTCOLOR  = BLUE          #┘

Tower_Color     = RED           #┐
Enemy_Color     = GRAY          #│
Road_Color      = GRAY          #│
Ground_Color    = GREEN         #│ Object Color
Shop_Color      = WHITE         #│
Gold_Color      = YELLOW        #│
Attack_Up_Color = RED           #│
Delay_Up_Color  = BLUE          #┘

SQUARE          = 'square'      #┐
TRIANGLE        = 'triangle'    #│ Define Shape 
PENTAGON        = 'pentagon'    #┘

REVEALSPEED     = 8              
BOXSIZE         = 40            
GAPSIZE         = 0             
BOARDWIDTH      = 16            
BOARDHEIGHT     = 11             
ShopWidth       = WINDOWWIDTH
ShopHeight      = 40

ShopSize        = [[0,0],[0,ShopWidth],[ShopHeight,ShopWidth],[ShopHeight,0]]   #Size

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH  * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT  * (BOXSIZE + GAPSIZE))) / 2)

def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)
    
def makemap():
    
    
def makeshop():
    pygame.draw.rect(DISPLAYSURF,Shop_Color,


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK    = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT ))
    DISPLAYSURF.fill(BGCOLOR)
    
    mousex      = 0
    mousey      = 0
    
    pygame.display.set_caption('Shape Defence Game')
    
    
    
    
    
    
if __name__ == '__main__': main()

    









































