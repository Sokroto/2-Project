from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('gb.jpg'), (700, 500))
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, image_pic, height, weight, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_pic), (height, weight))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
spr1 = GameSprite('rocketka.jpg', 65, 65, 0, 200, 5)
spr2 = GameSprite('rocketka.jpg', 65, 65, 600, 200, 5)
spr3 = GameSprite('ball.jpg', 40, 40, 600, 200, 7)
game = True
while game:
    clock.tick(FPS)
    window.blit(background, (0, 0))
    spr1.reset()
    spr2.reset()
    spr3.reset()
    
    display.update()