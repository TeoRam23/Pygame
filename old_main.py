import pygame as pg
from sprites import *
from random import randint


pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (30,150,30)
GREEN2 = (74,194,52)
BROWN = (230,198,119)
BLUE = (52,30,237,255)
RED = (236,43,49,255)
color = (255,255,255)



bush_group = pg.sprite.Group()
bushgull_group = pg.sprite.Group()
all_sprites = pg.sprite.Group()
eple_group = pg.sprite.Group()

jony = Player2()
jeffy = Player()

bush = EnemyBush()
bushgull = EnemyBushGull()
tre = EnemyTre()

eple = BadEple()

bush_group.add(bush)
bushgull_group.add(bushgull)
eple_group.add(eple)
all_sprites.add(bush, tre, jony, jeffy, eple, bushgull)


screen = pg.display.set_mode((WIDTH,HEIGHT))



FPS = 120
clock = pg.time.Clock()

SANS_Undertale30 = pg.font.SysFont("Calibri MS", 50)

text_hp1 = SANS_Undertale30.render("Jeffrey:" + str(jeffy.life), False, RED)

text_hp2 = SANS_Undertale30.render("Johnny:" + str(jony.life), False, BLUE)


playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    screen.fill(BROWN)


    all_sprites.update()


    hits = pg.sprite.spritecollide(jeffy, bush_group,True)
    hits2 = pg.sprite.spritecollide(jony, bush_group,True)
    hits3 = pg.sprite.spritecollide(jeffy, bushgull_group,True)
    hits4 = pg.sprite.spritecollide(jony, bushgull_group,True)
    hits5 = pg.sprite.spritecollide(jeffy, eple_group, True)
    hits6 = pg.sprite.spritecollide(jony, eple_group, True)


    

    if hits or hits3 or hits5:
        jeffy.life -= 1
        text_hp1 = SANS_Undertale30.render("Jeffrey:" + str(jeffy.life), False, RED)


    if jeffy.life <= 0:
        jeffy.kill()
        jeffy = Player()
        all_sprites.add(jeffy)

    if hits2 or hits4 or hits6:
        jony.life -=1
        text_hp2 = SANS_Undertale30.render("Johnny:" + str(jony.life), False, BLUE)

    if jony.life <= 0:
        jony.kill()
        jony = Player2()
        all_sprites.add(jony)



    # når mindre enn x busker er på skjermen kommer en ny en
    if len(bush_group) < 5:
        bush = EnemyBush()
        bush_group.add(bush)
        all_sprites.add(bush)

    if len(bushgull_group) < 5:
        waitgull = randint(1,50)
        if waitgull == 1:
            bushgull = EnemyBushGull()
            bushgull_group.add(bushgull)
            all_sprites.add(bushgull)

    if len(eple_group) < 1:
        eple = BadEple()
        eple_group.add(eple)
        all_sprites.add(eple)
    
    all_sprites.draw(screen)
    screen.blit(text_hp1, (10,10))
    screen.blit(text_hp2, (10,50))
    pg.display.update()