import random
from pygame import *


window = display.set_mode((500, 500))
display.set_caption("")
window.fill((255, 200, 200))
clock = time.Clock()

mixer.init()
win = mixer.Sound('sound/win.mp3')
win.set_volume(0.3)

win.play()


class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, w, h):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Coin(GameSprite):
    def __init__(self, filename, x, y, speed, w, h):
        GameSprite.__init__(self, filename, x, y, speed, w, h)
        self.counter = 0
        self.isPicked = False

    def animation(self):
        if self.isPicked:
            self.counter += 1
            if 0 <= self.counter < 30:
                self.image = transform.scale(image.load('pictures/Enemy_.png'), (self.w, self.h))
            elif 30 <= self.counter < 60:
                self.image = transform.scale(image.load('pictures/Portal.png'), (self.w, self.h))
            elif 60 <= self.counter < 75:
                self.image = transform.scale(image.load('pictures/Enemy_.png'), (self.w, self.h))
            elif 75 <= self.counter < 90:
                self.image = transform.scale(image.load('pictures/Portal.png'), (self.w, self.h))
            elif 90 <= self.counter < 95:
                self.image = transform.scale(image.load('pictures/Enemy_.png'), (self.w, self.h))
            elif 95 <= self.counter < 100:
                self.image = transform.scale(image.load('pictures/Portal.png'), (self.w, self.h))

            if self.counter == 100:
                coins.remove(self)

class Hero(GameSprite):
    def __init__(self, filename, x, y, speed, w, h):
        GameSprite.__init__(self, filename, x, y, speed, w, h)
        self.counter = 0

    def move(self, barells):
        keys = key.get_pressed()
        if keys[K_w]:
            if not self.check(self.rect.x, self.rect.y - self.speed, barells):
                self.rect.y -= self.speed
        elif keys[K_s]:
            if not self.check(self.rect.x, self.rect.y + self.speed, barells):
                self.rect.y += self.speed
        elif keys[K_a]:
            if not self.check(self.rect.x - self.speed, self.rect.y, barells):
                self.rect.x -= self.speed
        elif keys[K_d]:
            if not self.check(self.rect.x + self.speed, self.rect.y, barells):
                self.rect.x += self.speed
                self.animation('go_left')
        else:
            self.animation('stay')

    def animation(self, kind):
        if kind == 'stay':
            self.counter += 1
            if 0 <= self.counter < 10:
                self.image = transform.scale(image.load('pictures/player_w1.png'), (self.w, self.h))
            elif 10 <= self.counter < 20:
                self.image = transform.scale(image.load('pictures/player_w2.png'), (self.w, self.h))
            elif 20 <= self.counter < 30:
                self.image = transform.scale(image.load('pictures/player_w3.png'), (self.w, self.h))
            elif 30 <= self.counter < 40:
                self.image = transform.scale(image.load('pictures/player_w4.png'), (self.w, self.h))

            if self.counter > 40:
                self.counter = 0

        elif kind == 'go_left':
            self.counter += 1
            if 0 <= self.counter < 10:
                self.image = transform.scale(image.load('pictures/player_run_r1.png'), (self.w, self.h))
            elif 10 <= self.counter < 20:
                self.image = transform.scale(image.load('pictures/player_run_r2.png'), (self.w, self.h))
            elif 20 <= self.counter < 30:
                self.image = transform.scale(image.load('pictures/player_run_r3.png'), (self.w, self.h))
            elif 30 <= self.counter < 40:
                self.image = transform.scale(image.load('pictures/player_run_r4.png'), (self.w, self.h))
            elif 40 <= self.counter < 50:
                self.image = transform.scale(image.load('pictures/player_run_r5.png'), (self.w, self.h))
            elif 50 <= self.counter < 60:
                self.image = transform.scale(image.load('pictures/player_run_r6.png'), (self.w, self.h))

            if self.counter > 60:
                self.counter = 0

    def check(self, x, y, barells):
        barell_touch = []
        tmp_area = Rect(x, y, self.w, self.h)
        for barell in barells:
            barell.reset()
            barell_touch.append(barell.rect.colliderect(tmp_area))
        print(barell_touch, x, y)
        return True in barell_touch

hero = Hero('pictures/player_w1.png', 100, 200, 5, 80, 140)
barrel1 = GameSprite('pictures/Barrel_big.png', 200, 200, 0, 40, 50)
barrel2 = GameSprite('pictures/Barrel_big.png', 300, 200, 0, 40, 50)
barrel3 = GameSprite('pictures/Barrel_big.png', 400, 200, 0, 40, 50)
barells = [barrel1, barrel2, barrel3]

coin1 = Coin('pictures/Portal.png', 200, 300, 0, 80, 100)
coin2 = Coin('pictures/Portal.png', 300, 300, 0, 40, 50)
coin3 = Coin('pictures/Portal.png', 400, 300, 0, 40, 50)
coins = [coin1, coin2, coin3]

menu_bg = GameSprite('pictures/Menu_bg.png', 0, 0, 0, 500, 500)
btn_play = GameSprite('pictures/Button.png', 200, 200, 0, 100, 60)

btn_menu = GameSprite('pictures/Button_menu.png', 50, 50, 0, 50, 50)
game2_bg = GameSprite('pictures/game_bg (2).png', 0, 0, 0, 500, 500)

screen = 'menu'
next_screen = ''
timer = 60
game = True
while game:
    if screen == 'menu':
        menu_bg.reset()
        btn_play.reset()
        for e in event.get():
            if e.type == QUIT:
                game = False

            if e.type == MOUSEBUTTONDOWN:
                x, y = e.pos
                if btn_play.rect.collidepoint(x, y):
                    screen = 'game1'

        display.update()
        clock.tick(60)

    if screen == 'game1':
        window.fill((255, 200, 200))
        hero.reset()
        btn_menu.reset()

        for barell in barells:
            barell.reset()

        hero.move(barells)

        for coin in coins:
            coin.reset()
            coin.animation()
            if hero.rect.colliderect(coin.rect):
                coin.isPicked = True

        for e in event.get():
            if e.type == QUIT:
                screen = 'menu'

            if e.type == MOUSEBUTTONDOWN:
                x, y = e.pos
                if btn_menu.rect.collidepoint(x, y):
                    screen = 'menu'

            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    screen = 'menu'

        if hero.rect.x > 500:
            screen = 'transition'
            next_screen = 'game2'
            hero.rect.x = 20

        display.update()
        clock.tick(60)

    if screen == 'transition':
        window.fill((0, 0, 0, 0.5))

        for e in event.get():
            if e.type == QUIT:
                screen = 'menu'

        timer -= 1
        if timer == 0:
            screen = next_screen
            timer = 60

        display.update()
        clock.tick(60)

    if screen == 'game2':
        game2_bg.reset()
        btn_menu.reset()
        hero.reset()
        hero.move([])

        for e in event.get():
            if e.type == QUIT:
                game = False

            if e.type == MOUSEBUTTONDOWN:
                x, y = e.pos
                if btn_menu.rect.collidepoint(x, y):
                    screen = 'menu'

        if hero.rect.x < 0:
            screen = 'transition'
            next_screen = 'game1'
            hero.rect.x = 430

        display.update()
        clock.tick(60)