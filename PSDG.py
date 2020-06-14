import pygame, sys, random
from pygame.locals import *

FPS             = 60            #┐
WINDOWWIDTH     = 640           #│
WINDOWHEIGHT    = 480           #│
REVEALSPEED     = 8             #│ Define System Information 
BOXSIZE         = 40            #│
GAPSIZE         = 0             #│
BOARDWIDTH      = 10            #│
BOARDHEIGHT     = 7             #┘

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

Shop_Shape      = SQUARE

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH  * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT  * (BOXSIZE + GAPSIZE))) / 2)










































