from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = (self.image.get_rect())
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < height - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < height - 150:
            self.rect.y += self.speed

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption("Ping-Pong")
window = display.set_mode((width, height))
background = transform.scale(image.load('table.png'), (width, height))

clock = time.Clock()
FPS = 60

ball_x = 3
ball_y = 3

# score_l = 0
# score_r = 0

font.init()
font1 = font.SysFont("Arial", 36)
lose1 = font1.render("PLAYER LEFT LOSE!", True, (180, 0, 0))
lose2 = font1.render("PLAYER RIGHT LOSE!", True, (180, 0, 0))
# score_1 = font1.render("Score:", True, (180, 0, 0))
# score_2 = font1.render("Score:", True, (180, 0, 0))

# левая ракетка
racket1 = Player("rac.png", 10, 200, 50, 150, 4)
# правая ракетка
racket2 = Player("rac.png", 640, 200, 50, 150, 4)
# мяч
ball = GameSprite('asteroid.png', 330, 220, 80, 80, 4)

game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        # window.blit(score_1, (0, 20))
        # window.blit(score_2, (500, 20))
        ball.rect.x += ball_x
        ball.rect.y += ball_y
        if sprite.collide_rect(racket1, ball):
            ball_x *= -1
        if sprite.collide_rect(racket2, ball):
            ball_x *= -1
        if ball.rect.y > 420 or ball.rect.y < 0:
            ball_y *= -1
        if ball.rect.x > 750:
            finish = True
            window.blit(lose2, (200, 200))
        if ball.rect.x < -100:
            finish = True
            window.blit(lose1, (200, 200))

        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
