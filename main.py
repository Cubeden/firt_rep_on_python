from turtle import speed
from pygame import *
from random import randint

import pygame

mixer.init()
font.init()

win_width = 700
win_height = 500
mw = display.set_mode((win_width, win_height))
background = pygame.Surface((win_width, win_height))
background.fill((0, 0, 0))
mw.blit(background, (0,0))
display.set_caption('Maze | Слава Україні') 
clock = time.Clock()

mixer.music.load('music/background-music.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()
mixer.music.queue('music/background-music-2.mp3')
mixer.music.play()
lose = mixer.Sound('music/lose.mp3')
lose.set_volume(1)
win = mixer.Sound('music/win.mp3')
win.set_volume(1)

pause = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def move(self):
        key_p = key.get_pressed()
        if key_p[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

        if key_p[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if key_p[K_d] and self.rect.x < 668:
            self.rect.x += self.speed

        if key_p[K_RIGHT] and self.rect.x < 668:
            self.rect.x += self.speed

        if key_p[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if key_p[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if key_p[K_s] and self.rect.y < 468:
            self.rect.y += self.speed

        if key_p[K_DOWN] and self.rect.y < 468:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def move1(self):
        if self.rect.y <= 9:
            self.direction = 1

        elif self.rect.y >= 459:
            self.direction = 0

        if self.direction == 1:
            self.rect.y += self.speed
        if self.direction == 0:
            self.rect.y -= self.speed

    def move2(self):
        if self.rect.y <= 309:
            self.direction = 1

        elif self.rect.y >= 459 and self.direction == 1:
            self.direction = 0

        elif self.rect.x >= 209:
            self.direction = 2
        
        elif self.rect.x <= 59 and self.direction == 2:
            self.direction = 3

        if self.direction == 1:
            self.rect.y += self.speed
        if self.direction == 0:
            self.rect.x += self.speed
        if self.direction == 2:
            self.rect.x -= self.speed
        if self.direction == 3:
            self.rect.y -= self.speed

    def move3(self):
        if self.rect.y <= 59:
            self.direction = 1

        elif self.rect.y >= 209:
            self.direction = 0

        if self.direction == 1:
            self.rect.y += self.speed
        if self.direction == 0:
            self.rect.y -= self.speed

    def move4(self):
        if self.rect.x <= 109:
            self.direction = 1

        elif self.rect.x >= 159:
            self.direction = 0

        if self.direction == 1:
            self.rect.x += self.speed
        if self.direction == 0:
            self.rect.x -= self.speed

    def move5(self):
        if self.rect.x <= 209:
            self.direction = 1

        elif self.rect.x >= 459:
            self.direction = 0

        if self.direction == 1:
            self.rect.x += self.speed
        if self.direction == 0:
            self.rect.x -= self.speed

    def move6(self):
        if self.rect.y <= 159:
            self.direction = 1

        elif self.rect.y >= 259:
            self.direction = 0

        if self.direction == 1:
            self.rect.y += self.speed
        if self.direction == 0:
            self.rect.y -= self.speed

    def move7(self):
        if self.rect.y >= 459:
            self.direction = 1

        elif self.rect.y <= 409 and self.direction == 1:
            self.direction = 0

        elif self.rect.x >= 359:
            self.direction = 2
        
        elif self.rect.x <= 309 and self.direction == 2:
            self.direction = 3

        if self.direction == 1:
            self.rect.y -= self.speed
        if self.direction == 0:
            self.rect.x += self.speed
        if self.direction == 2:
            self.rect.x -= self.speed
        if self.direction == 3:
            self.rect.y += self.speed

    def move8(self):
        if self.rect.y >= 209:
            self.direction = 1

        elif self.rect.y <= 109:
            self.direction = 0

        if self.direction == 1:
            self.rect.y -= self.speed
        if self.direction == 0:
            self.rect.y += self.speed

    def move9(self):
        if self.rect.y <= 109:
            self.direction = 1

        elif self.rect.y >= 309:
            self.direction = 0

        if self.direction == 1:
            self.rect.y += self.speed
        if self.direction == 0:
            self.rect.y -= self.speed

    def move10(self):
        if self.rect.y <= 409:
            self.direction = 1

        elif self.rect.y >= 459:
            self.direction = 0

        if self.direction == 1:
            self.rect.y += self.speed
        if self.direction == 0:
            self.rect.y -= self.speed

    def move11(self):
        if self.rect.x <= 359:
            self.direction = 1

        elif self.rect.x >= 559:
            self.direction = 0

        if self.direction == 1:
            self.rect.x += self.speed
        if self.direction == 0:
            self.rect.x -= self.speed

    def move12(self):
        if self.rect.x <= 359:
            self.direction = 1

        elif self.rect.x >= 459:
            self.direction = 0

        if self.direction == 1:
            self.rect.x += self.speed
        if self.direction == 0:
            self.rect.x -= self.speed

    def move13(self):
        if self.rect.x <= 409:
            self.direction = 1

        elif self.rect.x >= 559:
            self.direction = 0

        if self.direction == 1:
            self.rect.x += self.speed
        if self.direction == 0:
            self.rect.x -= self.speed

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, x, y, W, H, color = (0, 122, 51)):
        super().__init__()
        self.color = color
        self.image = Surface((W, H))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    

walls = sprite.Group()

w_l = Wall(-2.5, 0, 5, 500)
w_r = Wall(697.5, 0, 5, 500)
w_u = Wall(0, -2.5, 700, 5)
w_d = Wall(0, 497.5, 700, 5)
w1 = Wall(47.5, 0, 5, 150)
w2 = Wall(47.5, 200, 5, 100)
w3 = Wall(47.5, 350, 5, 150)
w4 = Wall(97.5, 0, 5, 100)
w5 = Wall(97.5, 150, 5, 100)
w6 = Wall(97.5, 300, 5, 150)
w7 = Wall(47.5, 297.5, 55, 5)
w8 = Wall(147.5, 0, 5, 50)
w9 = Wall(147.5, 100, 5, 100)
w10 = Wall(147.5, 250, 5, 200)
w11 = Wall(97.5, 247.5, 55, 5)
w12 = Wall(97.5, 447.5, 55, 5)
w13 = Wall(197.5, 0, 5, 200)
w14 = Wall(197.5, 250, 5, 200)
w15 = Wall(147.5, 97.5, 105, 5)
w16 = Wall(147.5, 297.5, 55, 5)
w17 = Wall(247.5, 50, 5, 50)
w18 = Wall(247.5, 150, 5, 150)
w19 = Wall(247.5, 350, 5, 50)
w20 = Wall(197.5, 447.5, 105, 5)
w21 = Wall(297.5, 50, 5, 400)
w22 = Wall(247.5, 47.5, 55, 5)
w23 = Wall(247.5, 147.5, 55, 5)
w24 = Wall(247.5, 347.5, 55, 5)
w25 = Wall(347.5, 50, 5, 50)
w26 = Wall(347.5, 150, 5, 100)
w27 = Wall(347.5, 300, 5, 50)
w28 = Wall(297.5, 247.5, 55, 5)
w29 = Wall(297.5, 397.5, 105, 5)
w30 = Wall(397.5, 100, 5, 100)
w31 = Wall(397.5, 250, 5, 50)
w32 = Wall(397.5, 350, 5, 100)
w33 = Wall(347.5, 47.5, 105, 5)
w34 = Wall(347.5, 97.5, 55, 5)
w35 = Wall(347.5, 197.5, 55, 5)
w36 = Wall(347.5, 247.5, 55, 5)
w37 = Wall(347.5, 297.5, 55, 5)
w38 = Wall(347.5, 447.5, 55, 5)
w39 = Wall(447.5, 50, 5, 50)
w40 = Wall(447.5, 150, 5, 50)
w41 = Wall(447.5, 250, 5, 50)
w42 = Wall(447.5, 400, 5, 100)
w43 = Wall(397.5, 147.5, 205, 5)
w44 = Wall(397.5, 347.5, 255, 5)
w45 = Wall(497.5, 0, 5, 100)
w46 = Wall(497.5, 150, 5, 50)
w47 = Wall(497.5, 250, 5, 50)
w48 = Wall(497.5, 350, 5, 100)
w49 = Wall(447.5, 247.5, 55, 5)
w50 = Wall(547.5, 50, 5, 50)
w51 = Wall(547.5, 150, 5, 50)
w52 = Wall(547.5, 250, 5, 50)
w53 = Wall(547.5, 400, 5, 50)
w54 = Wall(497.5, 97.5, 55, 5)
w55 = Wall(497.5, 297.5, 55, 5)
w56 = Wall(497.5, 447.5, 55, 5)
w57 = Wall(597.5, 50, 5, 150)
w58 = Wall(597.5, 250, 5, 100)
w59 = Wall(597.5, 400, 5, 50)
w60 = Wall(647.5, 50, 5, 50)
w61 = Wall(647.5, 150, 5, 50)
w62 = Wall(647.5, 250, 5, 100)
w63 = Wall(647.5, 400, 5, 50)
w64 = Wall(597.5, 97.5, 55, 5)
w65 = Wall(597.5, 447.5, 55, 5)
walls.add(w_l, w_r, w_u, w_d, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25, w26, w27, w28, w29, w30, w31, w32, w33, w34, w35, w36, w37, w38, w39, w40, w41, w42, w43, w44, w45, w46, w47, w48, w49, w50, w51, w52, w53, w54, w55, w56, w57, w58, w59, w60, w61, w62, w63, w64, w65)


p = Player('img/player.png', 10, 250, 2.5, 32, 32)
e1 = Enemy('img/enemy.png', 659, 9, 2, 32, 32)
e2 = Enemy('img/enemy.png', 59, 309, 1, 32, 32)
e3 = Enemy('img/enemy.png', 59, 59, 1, 32, 32)
e4 = Enemy('img/enemy.png', 109, 59, 1, 32, 32)
e5 = Enemy('img/enemy.png', 209, 9, 2, 32, 32)
e6 = Enemy('img/enemy.png', 209, 159, 1, 32, 32)
e7 = Enemy('img/enemy.png', 309, 459, 2, 32, 32)
e8 = Enemy('img/enemy.png', 309, 209, 2, 32, 32)
e9 = Enemy('img/enemy.png', 609, 109, 2, 32, 32)
e10 = Enemy('img/enemy.png', 559, 409, 1, 32, 32)
e11 = Enemy('img/enemy.png', 359, 309, 1, 32, 32)
e12 = Enemy('img/enemy.png', 359, 209, 1, 32, 32)
e13 = Enemy('img/enemy.png', 409, 109, 1, 32, 32)
box = GameSprite('img/box.png', 359, 159, 0, 32, 32)
emblem = GameSprite('img/emblem-of-Ukraine.png', 0, 0, 0, 55, 75)

enemys = sprite.Group()
enemys.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13)


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_m:
                if pause == False:
                    pause = True

                else:
                    pause = False

    if pause:
        mixer.music.pause()
    else:
        mixer.music.unpause()
    
    if finish != True:
        mute_music = font.Font(None, 24).render('Mute/Unmute: M', True, (255,255, 255))
        mw.blit(background, (0,0))
        p.move()
        p.reset()
        e1.move1()
        e2.move2()
        e3.move3()
        e4.move4()
        e5.move5()
        e6.move6()
        e7.move7()
        e8.move8()
        e9.move9()
        e10.move10()
        e11.move11()
        e12.move12()
        e13.move13()
        for e in enemys:
            e.reset()
        box.reset()
        for w in walls:
            w.draw_wall()
        walls.update()
        mw.blit(mute_music, (568, 10))
        emblem.reset()

        if sprite.collide_rect(p, box):
            finish = True
            win_txt = font.Font(None, 64).render('YOU WIN', True, (255,255, 255))
            mw.blit(win_txt, (win_width/2 - 110, win_height/2 - 10))
            mixer.music.stop()
            win.play(-1)

        if sprite.spritecollide(p, walls, False) or sprite.spritecollide(p, enemys, False):
            finish = True
            win_txt = font.Font(None, 64).render('YOU LOSE', True, (255,255, 255))
            mw.blit(win_txt, (win_width/2 - 110, win_height/2 - 10))
            mixer.music.stop()
            lose.play()

    display.update()
    clock.tick(60)