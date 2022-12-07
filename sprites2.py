import pygame as pg
from random import randint
vec = pg.math.Vector2


player_img = pg.image.load("Jeffrey.png")
player_img = pg.transform.scale(player_img,(90,105)) #størrelsen på bildet
player_right_img = pg.transform.flip(player_img, True, False)
WALKING1 = pg.image.load("JeffreyWalk1.png")
WALKING1 = pg.transform.scale(WALKING1,(90,105))
WALKING2 = pg.image.load("JeffreyWalk2.png")
WALKING2 = pg.transform.scale(WALKING2,(90,105)) 



player2_img = pg.image.load("Johnny.png")
player2_img = pg.transform.scale(player2_img,(90,105)) #Størrelse på andre bildet
player2_right_img = pg.transform.flip(player2_img, True, False)



bush_img = pg.image.load("Busk.png")
bush_img = pg.transform.scale(bush_img,(105,95))
bush_left_img = pg.transform.flip(bush_img, True, False)


player_speed = 4

class Player(pg.sprite.Sprite):
    def __init__(self):
        self.groups = self.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = self
        self.current_frame = 0
        self.last_update = 0

        self.standing = True
        self.walking = False

        self.walking_frames = [player2_img, WALKING1, WALKING2]

        self.image = player_img

        self.image_right = player_right_img

        self.rect = self.image.get_rect() #henter self.image sin størrelse og rektangel
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 4

        self.life = 3
        

    def update(self):
        self.animate()
        self.rect.center = self.pos
        self.walking = True
        keys = pg.key.get_pressed()     
           
        if keys[pg.K_w]:
            self.pos.y -= player_speed
        if keys[pg.K_s]:
            self.pos.y += player_speed
        if keys[pg.K_a]:
            self.pos.x -= player_speed
            self.image = player_img
        if keys[pg.K_d]:
            self.pos.x += player_speed
            self.image = player_right_img

        #out of bounds
        if self.pos.x >= 755:
            self.pos.x = 755
        if self.pos.x <= 45:
            self.pos.x = 45
        if self.pos.y >= 748:
            self.pos.y = 748
        if self.pos.y <= 52:
            self.pos.y = 52


    def animate(self):
        now = pg.time.get_ticks()

        if self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.walking_frames)
                self.image = self.walking_frames[self.current_frame]
                self.rect = self.image.get_rect()




class Player2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player2_img

        self.image_left = player2_right_img

        self.rect = self.image.get_rect() #henter self.image sin størrelse og rektangel
        self.pos = vec(700,700)
        self.rect.center = self.pos
        self.speed = 4

        self.life = 3

    def update(self):
        self.rect.center = self.pos
        keys = pg.key.get_pressed()     
           
        if keys[pg.K_UP]:
            self.pos.y -= player_speed
        if keys[pg.K_DOWN]:
            self.pos.y += player_speed
        if keys[pg.K_LEFT]:
            self.pos.x -= player_speed
            self.image = player2_img
        if keys[pg.K_RIGHT]:
            self.pos.x += player_speed
            self.image = player2_right_img

        #andre out of bounds
        if self.pos.x >= 755:
            self.pos.x = 755
        if self.pos.x <= 45:
            self.pos.x = 45
        if self.pos.y >= 748:
            self.pos.y = 748
        if self.pos.y <= 52:
            self.pos.y = 52




class EnemyBush(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = bush_img

        self.image_left = bush_left_img

        self.pos = vec(-150,randint(50,750))
        self.rect =self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.walk = True
        self.walkcount = 0
        self.flip = 0

    def update(self):
        self.rect.center = self.pos

        if self.walk == True:
            self.walk = False
            self.rand = randint(1,5)
            self.speed = randint(1,2)

        #busk out of bounds
        if self.pos.y < 50:
            self.pos.y += self.speed
        if self.pos.y > 750:
            self.pos.y -= self.speed
        if self.pos.x < 50:
            self.pos.x += self.speed
        if self.pos.x > 750:
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

        self.flip += 1

        if self.flip <= 25:
            self.image = bush_img
        else:
            self.image = bush_left_img
        if self.flip > 50:
            self.flip = 0