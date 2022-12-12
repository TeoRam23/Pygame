import pygame as pg
from sprites import *

class Game():
    def __init__(self): # kjører når spillet starter
        pg.init()
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        GREEN = (30,150,30)
        GREEN2 = (74,194,52)
        self.BROWN = (230,198,119)
        self.BLUE = (52,30,237)
        self.RED = (236,43,49)


        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.bg = pg.image.load("BackGround.png").convert_alpha()
        self.bg = pg.transform.scale(self.bg,(WIDTH, HEIGHT))
        self.kant = pg.image.load("Kant.png").convert_alpha()
        self.kant = pg.transform.scale(self.kant,(WIDTH, HEIGHT))

        self.SANS_Undertale30 = pg.font.SysFont("Calibri MS", 50)
        self.FPS = 120
        self.clock = pg.time.Clock()
        
        self.new()


    def new(self): # ny runde
        self.bush_group = pg.sprite.Group()
        self.bushgull_group = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.eple_group = pg.sprite.Group()
        self.projectiles_grp = pg.sprite.Group()
        self.attack1_group = pg.sprite.Group()
        self.attack2_group = pg.sprite.Group()
        self.hurt_group = pg.sprite.Group()
        self.food_group = pg.sprite.Group()

        self.jony = Player2(self)
        self.jeffy = Player(self)

        self.bush = EnemyBush(self)
        self.bushgull = EnemyBushGull()
        self.tre = EnemyTre()

        self.eple = BadEple()

        self.bush_group.add(self.bush)
        self.bushgull_group.add(self.bushgull)
        self.eple_group.add(self.eple)

        self.hurt_group.add(self.bush, self.bushgull, self.eple)
    
        self.all_sprites.add(self.bush, self.tre, self.jony, self.jeffy, self.eple, self.bushgull)

        self.jeffy_poeng = 0
        self.jony_poeng = 0

        self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
        self.text_hp2 = self.SANS_Undertale30.render("Johnny:" + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

        self.eple_timer = 0
        self.attack2 = True

        self.poeng_timer = 0

        self.run()

    def run(self): # mens man spiller
        playing = True
        while playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        playing = False
                        self.new()

                    if event.key == pg.K_8:
                        self.jeffy.life = 99999
                        self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
                        self.jony.life = 99999
                        self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

                    if event.key == pg.K_TAB:
                        self.FPS = 12000
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_TAB:
                        self.FPS = 120

            self.screen.blit(self.bg,(0,0))

            self.all_sprites.update()

            hits = pg.sprite.spritecollide(self.jeffy, self.hurt_group,False)
            hits2 = pg.sprite.spritecollide(self.jony, self.hurt_group,False)
            food_hit = pg.sprite.spritecollide(self.jeffy, self.food_group, True)
            food_hit2 = pg.sprite.spritecollide(self.jony, self.food_group, True)

            poeng1 = pg.sprite.groupcollide(self.attack1_group, self.hurt_group, True, True)
            poeng2 = pg.sprite.groupcollide(self.attack2_group, self.hurt_group, True, True)

            pg.sprite.groupcollide(self.projectiles_grp, self.hurt_group,True, True)

            if food_hit:
                food_hit[0].give_health()
                self.jeffy_poeng += 25
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))

            if food_hit2:
                food_hit2[0].give_health2()
                self.jony_poeng += 10
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            if hits and self.jeffy.hurtTimer <= 0:
                self.jeffy.life -= 1
                self.jeffy_poeng -= 5
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))

            if self.jeffy.life <= 0:
                self.jeffy.kill()
                self.jeffy_poeng = 0
                self.jeffy = Player(self)
                self.all_sprites.add(self.jeffy)
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))

            if hits2 and self.jony.hurtTimer <= 0:
                self.jony.life -=1
                self.jony_poeng -= 5
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            if self.jony.life <= 0:
                self.jony.kill()
                self.jony_poeng = 0
                self.jony = Player2(self)
                self.all_sprites.add(self.jony)
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))


            if self.jeffy.life <= 0 and self.jony.life <= 0:
                playing = False
                self.new()

            if poeng1:
                self.jeffy_poeng += 15
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
            
            if poeng2:
                self.jony_poeng += 15
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))
            
            if self.poeng_timer > 240:
                self.poeng_timer = 0
                self.jeffy_poeng += 5
                self.jony_poeng += 5
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            if self.jeffy_poeng < 0:
                self.jeffy_poeng = 0
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
            if self.jony_poeng < 0:
                self.jony_poeng = 0
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            self.poeng_timer += 1

            # når mindre enn x busker er på skjermen kommer en ny en
            if len(self.bush_group) < 5:
                self.bush = EnemyBush(self)
                self.bush_group.add(self.bush)
                self.hurt_group.add(self.bush)
                self.all_sprites.add(self.bush)

            if len(self.bushgull_group) < 5:
                waitgull = randint(1,50)
                if waitgull == 1:
                    self.bushgull = EnemyBushGull()
                    self.bushgull_group.add(self.bushgull)
                    self.hurt_group.add(self.bushgull)
                    self.all_sprites.add(self.bushgull)

            self.eple_timer += 1
            if self.eple_timer >= 180:
                self.eple = BadEple()
                self.eple_group.add(self.eple)
                self.hurt_group.add(self.eple)
                self.all_sprites.add(self.eple)
                self.eple_timer = 0

            self.all_sprites.draw(self.screen)
            self.screen.blit(self.kant,(0,0))

            self.screen.blit(self.text_hp1, (10,10))
            self.screen.blit(self.text_hp2, (10,50))
            pg.display.update()

g = Game()