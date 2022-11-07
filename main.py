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
player_img = pg.image.load("Jeffrey3.png")
player_img = pg.transform.scale(player_img,(90,105)) #Størrelse på bildet

x = 30
y = 30

x2 = 670
y2 = 670

speed = 5

FPS = 120
clock = pg.time.Clock()

check = 0

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    screen.fill(GREEN)

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_a]:
        x -= speed
    if keys[pg.K_d]:
        x += speed

    if keys[pg.K_UP]:
        y2 -= speed
    if keys[pg.K_DOWN]:
        y2 += speed
    if keys[pg.K_LEFT]:
        x2 -= speed
    if keys[pg.K_RIGHT]:
        x2 += speed

#out of bounds
    if x >= 700:
        x = 700

    if x <= 0:
        x = 0

    if y >= 700:
        y = 700

    if y <= 0:
        y = 0


    if x2 >= 700:
        x2 = 700

    if x2 <= 0:
        x2 = 0

    if y2 >= 700:
        y2 = 700

    if y2 <= 0:
        y2 = 0           



    if x2 >= 700:
        rand12 = randint(-3,-2)
        direction_x2 = rand12
        color = (randint(0,255),randint(0,255),randint(0,255))

    if x2 <= 0:
        rand22 = randint(2,3)
        direction_x2 = rand22
        color = (randint(0,255),randint(0,255),randint(0,255))

    if y2 >= 700:
        rand32 = randint(-3,-2)
        direction_y2 = rand32
        color = (randint(0,255),randint(0,255),randint(0,255))

    if y2 <= 0:
        rand42 = randint(2,3)
        direction_y2 = rand42
        color = (randint(0,255),randint(0,255),randint(0,255))






    box2 = pg.Rect(x2,y2,100,100)
    pg.draw.rect(screen, RED, box2)


    screen.blit(player_img, (x,y))


    pg.display.update()