import pygame, sys, random
from pygame.locals import *

FPS = 60 


WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 0
BOARDWIDTH = 10
BOARDHEIGHT = 7

assert (BOARDWIDTH  * BOARDHEIGHT ) %2 ==0, '짝을 맞추기 위해서는 게임내 박스의 개수는 짝수개여야 합니다.'


XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH  * (BOXSIZE + GAPSIZE))) / 2)

YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT  * (BOXSIZE + GAPSIZE))) / 2)


GRAY = (100,100,100)
NAVYBLUE = (60,60,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
PURPLE = (255,0,255)
CYAN = (0,255,255)


BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE



DONUT = 'donut'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'



SQUARE = 'square'
TRIANGLE = 'triangle'
PENTAGON = 'pentagon'



ALLCOLOR = (RED, GREEN,BLUE ,YELLOW ,ORANGE ,PURPLE ,CYAN )
ALLSHAPE = (DONUT ,SQUARE ,DIAMOND ,LINES ,OVAL )

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT ))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False) 

    firstSelection = None
    DISPLAYSURF.fill(BGCOLOR)

    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True
                if firstSelection == None: 
                     firstSelection = (boxx, boxy)
                else: 
                    shape1, color1 = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    shape2, color2 = getShapeAndColor(mainBoard, boxx, boxy)

                    if shape1 != shape2 or color1 != color2:
                        pygame.time.wait(500) 
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes): 
                        pygame.time.wait(2000)

                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()

                        startGameAnimation(mainBoard)
                    firstSelection = None
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def hasWon(revealedBoxes):
    for i in revealedBoxes:    
        if False in i:
            return False 
    return True

def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def revealBoxesAnimation(board, boxGroup,coverage):
    for box in boxes :
        left, top = leftTopCoordsOfBox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF,BGCOLOR,(left, top, BOXSIZE, BOXSIZE))
        shape,color = getShapeAndColor(board,box[0],box[1])
        drawIcon(shape,color,box[0],box[1])
        if coverage>0:
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage,BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def drawBoxCovers(board, boxes, coverage):
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0:
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board, boxGroup):    
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxGroup, coverage)

def coverBoxesAnimation(board, boxGroup):
    for coverage in range(0 ,(BOXSIZE + REVEALSPEED) , REVEALSPEED):
        drawBoxCovers(board, boxGroup, coverage)

def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    boxGroups = []
    for i in range(0,len(boxes),8):
        boxGroups.append(boxes[i:i+8])

    drawBoard(board,coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)


def getShapeAndColor(board, boxx, boxy):
    return board[boxx][boxy][0], board[boxx][boxy][1]

def drawBoard(board, revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top =  leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)

def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE *0.25)
    half = int(BOXSIZE *0.5)

    left, top = leftTopCoordsOfBox(boxx, boxy)
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))





def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return ( left , top )

    
def generateRevealedBoxesData(val):
    revealedBoxes  =[]
    for i in range(BOARDWIDTH  ):
        revealedBoxes .append([val]*BOARDHEIGHT )
    return revealedBoxes  

def  getRandomizedBoard():
    icons = []
    for color in ALLCOLOR:
        for shape in ALLSHAPE:
            icons.append((shape,color))

    random.shuffle(icons)
    numIconsUsed = int(BOARDWIDTH  * BOARDHEIGHT/2)
    icons = icons[:numIconsUsed]*2
    random.shuffle(icons)
    
    board = []
    for x in range(BOARDWIDTH  ):
        column = []
        for y in range (BOARDHEIGHT ):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

if __name__ == '__main__':
    main()
    
    
    

















