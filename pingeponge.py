from pygame import *

font.init()
font = font.SysFont('Arial', 40)
R_win = font.render( 'NOPE LEFT SIDE LOSE', True, (255, 0, 0))
L_win = font.render( 'LOL RIGHT SIDE LOSE', True, (255, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        
class Ball(GameSprite):
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption("пинге понге")
run = True
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3
rocket1 = Player('racket.png', 10, 200, 80, 100, 5)
rocket2 = Player('racket.png', 610, 200, 80, 100, 5)
ball = Ball('ball.png', 320, 225, 50, 50, 5 )

finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False 

    window.fill((55, 55, 55))
    rocket1.update()
    rocket1.reset()
    rocket2.update2()
    rocket2.reset()
    ball.reset()

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y   

    if ball.rect.x > 700:
        window.blit(L_win, (200, 200))

    if ball.rect.x < -5:
        window.blit(R_win, (200, 200))

    if ball.rect.y > 450 or ball.rect.y <0:
        speed_y *= -1

    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
        speed_x *= -1

    for e in event.get():
        if e.type == QUIT:
            run = False

    clock.tick(FPS)
    display.update()