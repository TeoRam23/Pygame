import pygame as pg
from random import randint


pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (30,150,30)
BLUE = (10,80,230)
RED = (240,5,5)
color = (255,255,255)

screen = pg.display.set_mode((800,800))

x = 30
y = 30

x2 = 670
y2 = 400

direction_y = 2
direction_x = 2

direction_y2 = -3
direction_x2 = -3

check = 0

playing = True
while playing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    screen.fill(GREEN)


    check +=1
    if check == 6:
        check = 0
        x += direction_x
        y += direction_y
        x2 += direction_x2
        y2 += direction_y2      
          

    if x >= 700:
        rand1 = randint(-3,-2)
        direction_x = rand1
        color = (randint(0,255),randint(0,255),randint(0,255))

    if x >= x2-100 and y >= y2-100 and y <= y2+200:
        rand1 = randint(-3,-2)
        direction_x = rand1

            
    
    if x <= 0:
        rand2 = randint(2,3)
        direction_x = rand2
        color = (randint(0,255),randint(0,255),randint(0,255))

    if x <= x2-100 and y <= y2-100 and y >= y2+200:
        rand2 = randint(2,3)
        direction_x = rand2



    if y >= 700:
        rand3 = randint(-3,-2)
        direction_y = rand3
        color = (randint(0,255),randint(0,255),randint(0,255))

    if y >= y2-100 and x >= x2-100 and x <= x2+200:
        rand3 = randint(-3,-2)
        direction_y = rand3



    if y <= 0:
        rand4 = randint(2,3)
        direction_y = rand4
        color = (randint(0,255),randint(0,255),randint(0,255))
    
    if y >= y2-100 and x <= x2-100 and x >= x2+200:
        rand4 = randint(2,3)
        direction_y = rand4
            



    if x2 >= 700:
        rand12 = randint(-3,-2)
        direction_x2 = rand12
        color = (randint(0,255),randint(0,255),randint(0,255))

    if x2 >= x-100 and y2 >= y-100 and y2 <= y+200:
        rand12 = randint(-3,-2)
        direction_x2 = rand12

            
    
    if x2 <= 0:
        rand22 = randint(2,3)
        direction_x2 = rand22
        color = (randint(0,255),randint(0,255),randint(0,255))

    if x2 <= x-100 and y2 <= y-100 and y2 >= y+200:
        rand22 = randint(2,3)
        direction_x2 = rand22



    if y2 >= 700:
        rand32 = randint(-3,-2)
        direction_y2 = rand32
        color = (randint(0,255),randint(0,255),randint(0,255))

    if y2 >= y-100 and x2 >= x-100 and x2 <= x+200:
        rand32 = randint(-3,-2)
        direction_y2 = rand32



    if y2 <= 0:
        rand42 = randint(2,3)
        direction_y2 = rand42
        color = (randint(0,255),randint(0,255),randint(0,255))
    
    if y2 >= y-100 and x2 <= x-100 and x2 >= x+200:
        rand42 = randint(2,3)
        direction_y2 = rand42





    box2 = pg.Rect(x2,y2,100,100)
    pg.draw.rect(screen, RED, box2)

    box = pg.Rect(x,y,100,100)
    pg.draw.rect(screen, BLUE, box)


    pg.display.update()