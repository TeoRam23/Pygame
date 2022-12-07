import pygame as pg
from random import randint
vec = pg.math.Vector2

WIDTH = 901
HEIGHT = int(WIDTH/9*8)


player_width = 72
player_height = player_width*1.167

bush_width = 84
bush_height = bush_width*0.905

tre_width = 172
tre_height = tre_width*1.395

player_img = pg.image.load("Jeffrey.png")
player_img = pg.transform.scale(player_img,(player_width,player_height)) #størrelsen på bildet
player_right_img = pg.transform.flip(player_img, True, False)

playerWalk1 = pg.image.load("JeffreyWalk1.png")
playerWalk1 = pg.transform.scale(playerWalk1,(player_width,player_height)) #størrelsen på bildet
playerWalk1_right = pg.transform.flip(playerWalk1, True, False)

playerWalk2 = pg.image.load("JeffreyWalk2.png")
playerWalk2 = pg.transform.scale(playerWalk2,(player_width,player_height)) #størrelsen på bildet
playerWalk2_right = pg.transform.flip(playerWalk2, True, False)



player2_img = pg.image.load("Johnny.png")
player2_img = pg.transform.scale(player2_img,(player_width,player_height)) #Størrelse på andre bildet
player2_right_img = pg.transform.flip(player2_img, True, False)

player2Walk1 = pg.image.load("JohnnyWalk1.png")
player2Walk1 = pg.transform.scale(player2Walk1,(player_width,player_height)) #størrelsen på bildet
player2Walk1_right = pg.transform.flip(player2Walk1, True, False)

player2Walk2 = pg.image.load("JohnnyWalk2.png")
player2Walk2 = pg.transform.scale(player2Walk2,(player_width,player_height)) #størrelsen på bildet
player2Walk2_right = pg.transform.flip(player2Walk2, True, False)


playerHurt = pg.image.load("PlayerHurt.png")
playerHurt = pg.transform.scale(playerHurt,(player_width,player_height))
playerHurt_right = pg.transform.flip(playerHurt, True, False)

kylling_img = pg.image.load("Kylling.png")
kylling_img = pg.transform.scale(kylling_img,(player_width,player_width))


bush_img = pg.image.load("Busk.png")
bush_img = pg.transform.scale(bush_img,(bush_width, bush_height ))
bush_left_img = pg.transform.flip(bush_img, True, False)

bush2_img = pg.image.load("Busk2.png")
bush2_img = pg.transform.scale(bush2_img,(bush_width, bush_height ))


bushGull_img = pg.image.load("BuskGull.png")
bushGull_img = pg.transform.scale(bushGull_img,(bush_width, bush_height ))
bushGull_left_img = pg.transform.flip(bushGull_img, True, False)

bushGull2_img = pg.image.load("BuskGull2.png")
bushGull2_img = pg.transform.scale(bushGull2_img,(bush_width, bush_height ))



tre_img = pg.image.load("Tre.png")
tre_img = pg.transform.scale(tre_img,(tre_width, tre_height))

tre2_img = pg.image.load("Tre2.png")
tre2_img = pg.transform.scale(tre2_img,(tre_width, tre_height))

eple_img = pg.image.load("Eple.png")
eple_img = pg.transform.scale(eple_img,(36,36))



player_speed = 4
player_life = 5

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0
        self.last_update = 0

        self.standing = True
        self.standingRight = False
        self.walkingLeft = False
        self.walkingRight = False
        self.hurt = False
        self.hurtRight = False

        self.standing_frames = [player_img, player_img]
        self.standingRight_frames = [player_right_img, player_right_img]
        self.walkingLeft_frames = [playerWalk1, player_img, playerWalk2, player_img]
        self.walkingRight_frames = [playerWalk1_right, player_right_img, playerWalk2_right, player_right_img]

        self.image = player_img


        self.rect = self.image.get_rect() #henter self.image sin størrelse og rektangel
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 4

        self.life = player_life
        self.oldlife = self.life
        self.hurtTimer = 0
        self.hurtsies = 0
        
        self.last_x = self.pos.x
        self.last_y = self.pos.y
        self.last_direct = 1

        self.projectile_speed = 5

        self.attack_direction_x = -self.projectile_speed
        self.attack_direction_y = 0



    def update(self):
        self.animate()

        self.rect.center = self.pos

        keys = pg.key.get_pressed()
           
        if self.last_direct == 1:
            if keys[pg.K_w] or keys[pg.K_s]:
                self.walkingLeft = True
                self.standing = False
                self.standingRight = False         

        if self.last_direct == 2:
            if keys[pg.K_w] or keys[pg.K_s]:
                self.walkingRight = True
                self.standing = False
                self.standingRight = False

        if keys[pg.K_w]:
            self.pos.y -= player_speed
            self.attack_direction_y = -self.projectile_speed
            self.attack_direction_x = 0
        if keys[pg.K_s]:
            self.pos.y += player_speed
            self.attack_direction_y = self.projectile_speed
            self.attack_direction_x = 0
        if keys[pg.K_a]:
            self.pos.x -= player_speed
            self.walkingLeft = True
            self.standing = False
            self.standingRight = False
            self.attack_direction_x = -self.projectile_speed
            self.attack_direction_y = 0
        if keys[pg.K_d]:
            self.pos.x += player_speed
            self.walkingRight = True
            self.walkingLeft = False
            self.standing = False
            self.standingRight = False
            self.attack_direction_x = self.projectile_speed
            self.attack_direction_y = 0

        if keys[pg.K_f]:
            self.attack()


        #out of bounds
        if self.pos.x >= WIDTH-(player_width/2):
            self.pos.x = WIDTH-(player_width/2)
        if self.pos.x <= player_width/2:
            self.pos.x = player_width/2
        if self.pos.y >= HEIGHT-(player_height/2):
            self.pos.y = HEIGHT-(player_height/2)
        if self.pos.y <= player_height/2:
            self.pos.y = player_height/2

        
        if self.pos.x == self.last_x and self.pos.y == self.last_y:
            self.walkingLeft = False
            self.walkingRight = False
            if self.last_direct == 1:
                self.standing = True
                self.standingRight = False
            if self.last_direct == 2:
                self.standingRight = True
                self.standing = False

        self.last_x = self.pos.x
        self.last_y = self.pos.y

        

        if self.life < self.oldlife and self.life != 0:
            self.walkingLeft = False
            self.walkingRight = False
            self.hurtsies += 1
            if self.last_direct == 1:
                self.hurt = True
            if self.last_direct == 2:
                self.hurtRight = True
        if self.hurtsies >= 1:
            self.hurtTimer += 1
        if self.oldlife == self.life and self.hurtTimer > 60:
            self.hurt = False
            self.hurtRight = False
            self.hurtTimer = 0
            self.hurtsies = 0
            

        self.oldlife = self.life

    def attack(self):
        attack_obj = Ranged_attack(self.game, self.pos.x, self.pos.y, self.attack_direction_x, self.attack_direction_y)


    def animate(self):
        now = pg.time.get_ticks()

        if self.walkingLeft:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.walkingLeft_frames)
                self.image = self.walkingLeft_frames[self.current_frame]
                self.rect = self.image.get_rect()

                self.last_direct = 1

        if self.walkingRight:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.walkingRight_frames)
                self.image = self.walkingRight_frames[self.current_frame]
                self.rect = self.image.get_rect()

                self.last_direct = 2
        
        if self.standing:
            self.current_frame = (self.current_frame + 1)% len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()

        if self.standingRight:
            self.current_frame = (self.current_frame + 1)% len(self.standingRight_frames)
            self.image = self.standingRight_frames[self.current_frame]
            self.rect = self.image.get_rect()


        if self.hurt:
            self.image = playerHurt
            self.rect = self.image.get_rect()
        
        if self.hurtRight:
            self.image = playerHurt_right
            self.rect = self.image.get_rect()


class Player2(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0
        self.last_update = 0

        self.standing = True
        self.standingRight = False
        self.walkingLeft = False
        self.walkingRight = False
        self.hurt = False
        self.hurtRight = False

        self.standing_frames = [player2_img, player2_img]
        self.standingRight_frames = [player2_right_img, player2_right_img]
        self.walkingLeft_frames = [player2Walk1, player2_img, player2Walk2, player2_img]
        self.walkingRight_frames = [player2Walk1_right, player2_right_img, player2Walk2_right, player2_right_img]
        self.image = player2_img

        self.image_left = player2_right_img

        self.rect = self.image.get_rect() #henter self.image sin størrelse og rektangel
        self.pos = vec(WIDTH-100,HEIGHT-100)
        self.rect.center = self.pos
        self.speed = 4

        self.life = player_life
        self.oldlife = self.life
        self.hurtTimer = 0
        self.hurtsies = 0

        self.last_x = self.pos.x
        self.last_y = self.pos.y
        self.last_direct = 1

        self.projectile_speed = 5

        self.attack_direction_x = -self.projectile_speed
        self.attack_direction_y = 0

    def update(self):
        self.animate()
        self.rect.center = self.pos
        keys = pg.key.get_pressed()     

        if self.last_direct == 1:
            if keys[pg.K_UP] or keys[pg.K_DOWN]:
                self.walkingLeft = True
                self.standing = False
                self.standingRight = False         

        if self.last_direct == 2:
            if keys[pg.K_UP] or keys[pg.K_DOWN]:
                self.walkingRight = True
                self.standing = False
                self.standingRight = False  


           
        if keys[pg.K_UP]:
            self.pos.y -= player_speed
            self.attack_direction_y = -self.projectile_speed
            self.attack_direction_x = 0
        if keys[pg.K_DOWN]:
            self.pos.y += player_speed
            self.attack_direction_y = self.projectile_speed
            self.attack_direction_x = 0
        if keys[pg.K_LEFT]:
            self.pos.x -= player_speed
            self.walkingLeft = True
            self.standing = False
            self.standingRight = False
            self.attack_direction_x = -self.projectile_speed
            self.attack_direction_y = 0
        if keys[pg.K_RIGHT]:
            self.pos.x += player_speed
            self.walkingRight = True
            self.walkingLeft = False
            self.standing = False
            self.standingRight = False
            self.attack_direction_x = self.projectile_speed
            self.attack_direction_y = 0

        if keys[pg.K_RCTRL]:
            self.attack()

        #andre out of bounds
        if self.pos.x >= WIDTH-(player_width/2):
            self.pos.x = WIDTH-(player_width/2)
        if self.pos.x <= player_width/2:
            self.pos.x = player_width/2
        if self.pos.y >= HEIGHT-(player_height/2):
            self.pos.y = HEIGHT-(player_height/2)
        if self.pos.y <= player_height/2:
            self.pos.y = player_height/2

        
        if self.pos.x == self.last_x and self.pos.y == self.last_y:
            self.walkingLeft = False
            self.walkingRight = False
            if self.last_direct == 1:
                self.standing = True
                self.standingRight = False
            if self.last_direct == 2:
                self.standingRight = True
                self.standing = False

        self.last_x = self.pos.x
        self.last_y = self.pos.y


        if self.life < self.oldlife and self.life != 0:
            self.walkingLeft = False
            self.walkingRight = False
            self.hurtsies += 1
            if self.last_direct == 1:
                self.hurt = True
            if self.last_direct == 2:
                self.hurtRight = True
        if self.hurtsies >= 1:
            self.hurtTimer += 1
        if self.oldlife == self.life and self.hurtTimer > 60:
            self.hurt = False
            self.hurtRight = False
            self.hurtTimer = 0
            self.hurtsies = 0

        self.oldlife = self.life


    def animate(self):
        now = pg.time.get_ticks()

        if self.walkingLeft:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.walkingLeft_frames)
                self.image = self.walkingLeft_frames[self.current_frame]
                self.rect = self.image.get_rect()

                self.last_direct = 1

        if self.walkingRight:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.walkingRight_frames)
                self.image = self.walkingRight_frames[self.current_frame]
                self.rect = self.image.get_rect()

                self.last_direct = 2

        
        if self.standing:
            self.current_frame = (self.current_frame + 1)% len(self.standing_frames)
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()

        if self.standingRight:
            self.current_frame = (self.current_frame + 1)% len(self.standingRight_frames)
            self.image = self.standingRight_frames[self.current_frame]
            self.rect = self.image.get_rect()

        if self.hurt:
            
            self.image = playerHurt
            self.rect = self.image.get_rect()
        
        if self.hurtRight:
            self.image = playerHurt_right
            self.rect = self.image.get_rect()

    def attack(self):
        attack_obj = Ranged_attack(self.game, self.pos.x, self.pos.y, self.attack_direction_x,self.attack_direction_y)


class EnemyBush(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.current_frame = 0
        self.last_update = 0

        self.wiggle = True

        self.wiggle_frames = [bush_img, bush2_img]

        self.image = bush_img

        self.image_left = bush_left_img

        self.pos = vec(-150,randint(50,HEIGHT-50))
        self.rect =self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.walk = True
        self.walkcount = 0


    def update(self):
        self.animate()
        self.rect.center = self.pos

        if self.walk == True:
            self.walk = False
            self.rand = randint(1,5)
            self.speed = randint(1,2)

        #busk out of bounds
        if self.pos.y < bush_height/2:
            self.pos.y += self.speed
        if self.pos.y > HEIGHT - (bush_height/2):
            self.pos.y -= self.speed
        if self.pos.x < bush_width/2:
            self.pos.x += self.speed
        if self.pos.x > WIDTH - (bush_width/2):
            self.pos.x -= self.speed
            
        #går tilfeldig sted
        if self.rand == 1:
            self.pos.y -= self.speed
        elif self.rand == 2:
            self.pos.x += self.speed
        elif self.rand == 3:
            self.pos.y += self.speed
        elif self.rand == 4:
            self.pos.x -= self.speed
        elif self.rand == 5:
            self.pos == self.pos


        self.walkcount += 1

        if self.rand != 5 and self.walkcount >= 100:
            self.walk = True
            self.walkcount = 0
        elif self.walkcount >= 50:
            self.walk = True
            self.walkcount = 0

        keys = pg.key.get_pressed()
        if keys[pg.K_p]:
            self.summon()



    def summon(self):
        summon_obj = LittMat(self.game, self.pos.x, self.pos.y)


    def animate(self):
        now = pg.time.get_ticks()

        if self.wiggle:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.wiggle_frames)
                self.image = self.wiggle_frames[self.current_frame]
                self.rect = self.image.get_rect()

    

class EnemyBushGull(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0

        self.wiggle = True

        self.wiggle_frames = [bushGull_img, bushGull2_img]

        self.image = bush_img

        self.image_left = bush_left_img

        self.randpos = randint(1,2)
        if self.randpos == 1:
            self.pos = vec(randint(150,WIDTH+50),-50)
        else:
            self.pos = vec(WIDTH+50,randint(-50, HEIGHT-150))            

        self.rect =self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 1
        self.walk = True
        self.walkcount = 0

    def update(self):
        self.animate()
        self.rect.center = self.pos
        self.pos.x -= self.speed
        self.pos.y += self.speed

        if self.pos.x < -30 or self.pos.y > HEIGHT+30:
            self.kill()



    def animate(self):
        now = pg.time.get_ticks()

        if self.wiggle:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.wiggle_frames)
                self.image = self.wiggle_frames[self.current_frame]
                self.rect = self.image.get_rect()



class EnemyTre(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0

        self.wiggle = True

        self.wiggle_frames = [tre_img, tre2_img]

        self.image = tre_img

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.rect =self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.animate()

        self.rect.center = self.pos

    
    def attack(self):
        pass
   
   
    def animate(self):
        now = pg.time.get_ticks()

        if self.wiggle:
            if now - self.last_update > 250:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.wiggle_frames)
                self.image = self.wiggle_frames[self.current_frame]
                self.rect = self.image.get_rect()



class BadEple(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = eple_img
        self.orig_img = self.image

        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2+tre_height/4)
        self.rect.center = self.pos
        self.speed = 2
        self.direct = randint(1,8)
        self.direction = 1
        self.angle = 0
        self.angle_speed = randint(-3,3)
        if self.angle_speed == 0:
            self.angle_speed = 1

        self.wait = 0

    def update(self):
        self.rect.center = self.pos
        self.angle += self.angle_speed

        self.image, self.rect = self.rot_center(self.orig_img, self.angle, self.pos.x, self.pos.y)

        if self.direct == 1:
            self.pos.y -= self.speed/1.5
            self.pos.x += self.speed/1.5
        if self.direct == 2:
            self.pos.x += self.speed
        if self.direct == 3:
            self.pos.y += self.speed/1.5
            self.pos.x += self.speed/1.5
        if self.direct == 4:
            self.pos.y += self.speed
        if self.direct == 5:
            self.pos.y += self.speed/1.5
            self.pos.x -= self.speed/1.5
        if self.direct == 6:
            self.pos.x -= self.speed
        if self.direct == 7:
            self.pos.y -= self.speed/1.5
            self.pos.x -= self.speed/1.5
        if self.direct == 8:
            self.pos.y -= self.speed

        if self.pos.x > WIDTH+30 or self.pos.x < -30:
            self.kill()
        if self.pos.y > HEIGHT+30 or self.pos.y < -30:
            self.kill()

    def rot_center(self, image, angle, x, y):
        rotated_image = pg.transform.rotate(image, angle)
        self.new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (x,y)).center)

        return rotated_image, self.new_rect



class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, x ,y, direction_x, direction_y):
        self.groups = game.all_sprites, game.projectiles_grp # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface([50,50])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) # start posisjon
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.rect.center = self.pos
 
    def update(self):
        self.rect.center = self.pos
        self.pos.x += self.direction_x
        self.pos.y += self.direction_y


class LittMat(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.food_group # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = kylling_img
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.rect.center = self.pos
 
    def update(self):
        self.rect.center = self.pos
 
    def give_health(self):
        self.game.jeffy.life += 2

    def give_health2(self):
        self.game.jony.life += 2


class test(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = bush_img

        self.image_left = bush_left_img

        self.randpos = randint(1,2)
        if self.randpos == 1:
            self.pos = vec(randint(150,WIDTH+50),-50)
        else:
            self.pos = vec(WIDTH+50,randint(-50, HEIGHT-150))            

        self.rect =self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 1
        self.walk = True
        self.walkcount = 0

    def update(self):
        self.move_to = vec(pg.mouse.get_pos()) # finner posisjon til musepeker
        self.move_vector = self.move_to - self.pos  # finner "forskjellen" mellom self.pos og posisjon til musepeker
        self.pos += self.move_vector.normalize() * self.speed  # flytter self.pos litt mot musepeker
        self.rect.center = self.pos