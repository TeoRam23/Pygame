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

        pg.mixer.music.load("music_main.wav")
        pg.mixer.music.set_volume(0.2)

        self.hurt_sound = pg.mixer.Sound("sound_hurt.wav")
        self.hurt_sound.set_volume(0.5) 

        self.eat_sound = pg.mixer.Sound("sound_eat.wav")
        self.eat_sound.set_volume(0.3)

        self.zap_sound = pg.mixer.Sound("sound_zap.wav")
        self.zap_sound.set_volume(0.5)

        self.bush_sound = pg.mixer.Sound("sound_bush.wav")
        self.bush_sound.set_volume(0.4)

        self.apple_sound = pg.mixer.Sound("sound_apple.wav")
        self.apple_sound.set_volume(0.4)

        self.start_sound = pg.mixer.Sound("sound_start.wav")
        self.start_sound.set_volume(0.5)

        self.death_sound = pg.mixer.Sound("sound_death.wav")
        self.death_sound.set_volume(0.3)

        self.end_sound = pg.mixer.Sound("sound_end.wav")
        self.end_sound.set_volume(0.5)

        self.start_screen = pg.image.load("Start.png").convert_alpha()
        self.start_screen = pg.transform.scale(self.start_screen,(WIDTH, HEIGHT))
        self.show_poeng = False
        self.score_board1 = 0
        self.score_board2 = 0

        self.SANS_Undertale30 = pg.font.SysFont("Calibri MS", 50)
        self.FPS = 120
        self.clock = pg.time.Clock()

        self.quit = False
        
        self.start()

    def start(self): # strarten av spillet og vises etter at man dør
        press_space = True
        start_game = False
        self.duel = False
        pg.mixer.music.stop()
        
        while press_space:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    press_space = False
                    self.quit = True
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        press_space = False
                        start_game = True
                    if event.key == pg.K_o:
                        press_space = False
                        start_game = True
                        self.duel = True
            
            self.screen.blit(self.start_screen,(0,0))

            if self.show_poeng:
                if self.winner1:
                    self.score_board1 = self.SANS_Undertale30.render("W|Jeffrey poeng: " + str(self.jeffy_poeng), False, (self.RED))
                    self.score_board2 = self.SANS_Undertale30.render("L|Johnny poeng: " + str(self.jony_poeng), False, (self.BLUE))
                if self.winner2:
                    self.score_board1 = self.SANS_Undertale30.render("L|Jeffrey poeng: " + str(self.jeffy_poeng), False, (self.RED))
                    self.score_board2 = self.SANS_Undertale30.render("W|Johnny poeng: " + str(self.jony_poeng), False, (self.BLUE))
                if self.winner1 == False and self.winner2 == False:
                    self.score_board1 = self.SANS_Undertale30.render("Jeffrey poeng: " + str(self.jeffy_poeng), False, (self.RED))
                    self.score_board2 = self.SANS_Undertale30.render("Johnny poeng: " + str(self.jony_poeng), False, (self.BLUE))

                self.screen.blit(self.score_board1, (WIDTH/3,HEIGHT/2+100))
                self.screen.blit(self.score_board2, (WIDTH/3,HEIGHT/2+150))
            
            if self.show_poeng == False:
                self.score_board1 = self.SANS_Undertale30.render("Jeffrey kontroll: WASD | F = skyt ball", False, (self.RED))
                self.score_board2 = self.SANS_Undertale30.render("Johnny kontroll: piltaster | ctrlR = shyt ball", False, (self.BLUE))
                self.screen.blit(self.score_board1, (150,HEIGHT/2+100))
                self.screen.blit(self.score_board2, (120,HEIGHT/2+150))


            pg.display.update()

            if start_game:
                start_game = False
                self.show_poeng = False
                pg.mixer.Sound.play(self.start_sound)
                self.new()
            


    def new(self): # ny runde
        self.bush_group = pg.sprite.Group()
        self.bushgull_group = pg.sprite.Group()
        self.bush_group_full = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.eple_group = pg.sprite.Group()
        self.projectiles_grp = pg.sprite.Group()
        self.attack1_group = pg.sprite.Group()
        self.attack2_group = pg.sprite.Group()
        self.hurt_group = pg.sprite.Group()
        self.food_group = pg.sprite.Group()

        self.player_group_full = pg.sprite.Group()

        self.harder = False

        self.jony = Player2(self)
        self.jeffy = Player(self)

        self.bush = EnemyBush(self)
        self.bushgull = EnemyBushGull(self)
        self.tre = EnemyTre(self)

        self.eple = BadEple(self)

        self.bush_group.add(self.bush)
        self.bushgull_group.add(self.bushgull)
        self.bush_group_full.add(self.bush, self.bushgull)
        self.eple_group.add(self.eple)

        self.hurt_group.add(self.bush, self.bushgull, self.eple)
    
        self.all_sprites.add(self.bush, self.tre, self.eple, self.bushgull)

        self.jeffy_poeng = 0
        self.jony_poeng = 0

        self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
        self.text_hp2 = self.SANS_Undertale30.render("Johnny:" + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

        self.eple_timer = 0
        self.attack2 = True

        self.timer = 0

        self.poeng_timer = 0
        self.winner1 = False
        self.winner2 = False
        self.run()

    def run(self): # mens man spiller
        self.playing = True
        self.show_poeng = True
        pg.mixer.music.play(-1) 
        while self.playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.playing = False
                        self.show_poeng = False
                        self.start()
                    # skrur manuelt på harder modus
                    if event.key == pg.K_BACKSPACE:
                        self.harder = True
                    # gir deg 99999 liv
                    if event.key == pg.K_8:
                        if self.jeffy.death:
                            self.jeffy.death = False
                            self.jeffy = Player(self)
                        self.jeffy.life = 99999
                        self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
                        if self.jony.death:
                            self.jony.death = False
                            self.jony = Player2(self)
                        self.jony.life = 99999
                        self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            self.screen.blit(self.bg,(0,0))

            self.all_sprites.update()

            hits = pg.sprite.spritecollide(self.jeffy, self.hurt_group,False)
            hits2 = pg.sprite.spritecollide(self.jony, self.hurt_group,False)
            food_hit = pg.sprite.spritecollide(self.jeffy, self.food_group, True)
            food_hit2 = pg.sprite.spritecollide(self.jony, self.food_group, True)

            bush_hit = pg.sprite.groupcollide(self.projectiles_grp, self.bush_group_full, False, False)
            eple_hit = pg.sprite.groupcollide(self.projectiles_grp, self.eple_group, False, False)

            poeng1 = pg.sprite.groupcollide(self.attack1_group, self.hurt_group, True, True)
            poeng2 = pg.sprite.groupcollide(self.attack2_group, self.hurt_group, True, True)

            pg.sprite.groupcollide(self.projectiles_grp, self.hurt_group,True, True)

            # brukes til å få spillerne til å skade hverandre
            if self.duel:
                if self.jeffy.death == False:
                    broHit1 = pg.sprite.spritecollide(self.jeffy, self.attack2_group, True, False)
                    if broHit1 and self.duel and self.jeffy.hurtTimer <= 0 and self.jeffy.death == False:
                        self.jeffy.life -= 1
                        self.jeffy_poeng -= 5
                        self.jony_poeng += 5
                        pg.mixer.Sound.play(self.hurt_sound)
                        self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
                
                if self.jony.death == False:
                    broHit2 = pg.sprite.spritecollide(self.jony, self.attack1_group, True, False)
                    if broHit2 and self.duel and self.jony.hurtTimer <= 0 and self.jony.death == False:
                        self.jony.life -=1
                        self.jony_poeng -= 5
                        self.jeffy_poeng += 5
                        pg.mixer.Sound.play(self.hurt_sound)
                        self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            # når jeffrey får mat
            if food_hit and self.jeffy.death == False:
                food_hit[0].give_health()
                self.jeffy_poeng += 10
                pg.mixer.Sound.play(self.eat_sound)
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
            # når johnny får mat
            if food_hit2 and self.jony.death == False:
                food_hit2[0].give_health2()
                self.jony_poeng += 10
                pg.mixer.Sound.play(self.eat_sound)
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))
            # når jeffrey blir truffet og hurt timeren er på 0 og Jeffrey ikke er død
            if hits and self.jeffy.hurtTimer <= 0 and self.jeffy.death == False:
                self.jeffy.life -= 1
                self.jeffy_poeng -= 5
                pg.mixer.Sound.play(self.hurt_sound)
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))

            if self.jeffy.life <= 0:
                self.jeffy.kill()
                if self.jeffy.death == False and self.jony.death == False:
                    pg.mixer.Sound.play(self.death_sound)
                self.jeffy.death = True
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Død " + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
                if self.duel and self.winner1 == False:
                    self.winner2 = True

            if hits2 and self.jony.hurtTimer <= 0 and self.jony.death == False:
                self.jony.life -=1
                self.jony_poeng -= 5
                pg.mixer.Sound.play(self.hurt_sound)
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            if self.jony.life <= 0:
                self.jony.kill()
                if self.jony.death == False and self.jeffy.death == False:
                    pg.mixer.Sound.play(self.death_sound)
                self.jony.death = True
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Død " + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))
                if self.duel and self.winner2 == False:
                    self.winner1 = True
            # når begge spillerne har dødd
            if self.jeffy.death and self.jony.death and self.quit == False:
                self.playing = False
                if self.jeffy_poeng < 0:
                    self.jeffy_poeng = 0
                if self.jony_poeng < 0:
                    self.jony_poeng = 0
                pg.mixer.Sound.play(self.end_sound)
                self.start()

            if poeng1:
                self.jeffy_poeng += 15
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
            
            if poeng2:
                self.jony_poeng += 15
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))
            
            # hvert 240 tick får man 5 poeng
            if self.poeng_timer > 240:
                self.poeng_timer = 0
                if self.jeffy.death == False:
                    self.jeffy_poeng += 5
                    self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
                if self.jony.death == False:
                    self.jony_poeng += 5
                    self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))
            # når man har mindre enn 0 poeng får man 0 poeng sånn at man ikke kan ha mindre enn 0 poeng
            if self.jeffy_poeng < 0:
                self.jeffy_poeng = 0
                self.text_hp1 = self.SANS_Undertale30.render("Jeffrey: Liv " + str(self.jeffy.life) + "|Poeng " + str(self.jeffy_poeng), False, (self.RED))
            if self.jony_poeng < 0:
                self.jony_poeng = 0
                self.text_hp2 = self.SANS_Undertale30.render("Johnny: Liv " + str(self.jony.life) + "|Poeng " + str(self.jony_poeng), False, (self.BLUE))

            self.poeng_timer += 1


            # når mindre enn 5 busker er på skjermen kommer en ny en
            if len(self.bush_group) < 5 and self.harder == False:
                self.bush = EnemyBush(self)
                self.bush_group.add(self.bush)
                self.bush_group_full.add(self.bush)
                self.hurt_group.add(self.bush)
                self.all_sprites.add(self.bush)
            if len(self.bush_group) < 7 and self.harder:
                self.bush = EnemyBush(self)
                self.bush_group.add(self.bush)
                self.bush_group_full.add(self.bush)
                self.hurt_group.add(self.bush)
                self.all_sprites.add(self.bush)

            if len(self.bushgull_group) < 5 and self.harder == False:
                waitgull = randint(1,50)
                if waitgull == 1:
                    self.bushgull = EnemyBushGull(self)
                    self.bushgull_group.add(self.bushgull)
                    self.bush_group_full.add(self.bushgull)
                    self.hurt_group.add(self.bushgull)
                    self.all_sprites.add(self.bushgull)
            if len(self.bushgull_group) < 7 and self.harder:
                waitgull = randint(1,50)
                if waitgull == 1:
                    self.bushgull = EnemyBushGull(self)
                    self.bushgull_group.add(self.bushgull)
                    self.bush_group_full.add(self.bushgull)
                    self.hurt_group.add(self.bushgull)
                    self.all_sprites.add(self.bushgull)

            # hvert 180 tick spawner et nytt eple
            self.eple_timer += 1
            if self.harder == False and self.eple_timer >= 180:
                self.eple = BadEple(self)
                self.eple_group.add(self.eple)
                self.hurt_group.add(self.eple)
                self.all_sprites.add(self.eple)
                self.eple_timer = 0
            if self.harder and self.eple_timer >= 130:
                self.eple = BadEple(self)
                self.eple_group.add(self.eple)
                self.hurt_group.add(self.eple)
                self.all_sprites.add(self.eple)
                self.eple_timer = 0

            if bush_hit:
                pg.mixer.Sound.play(self.bush_sound)
            if eple_hit:
                pg.mixer.Sound.play(self.apple_sound)
            # etter en hvis tid starter harder modus
            if self.harder == False:
                self.timer += 1
            if self.timer == 7000:
                self.harder = True

            self.all_sprites.draw(self.screen)
            self.screen.blit(self.kant,(0,0))

            self.screen.blit(self.text_hp1, (10,10))
            self.screen.blit(self.text_hp2, (10,50))
            pg.display.update()

g = Game()