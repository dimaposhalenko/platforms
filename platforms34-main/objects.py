from settings import *

class MapObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))




        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = x










class Button:
    def __init__(self, x, y, w, h, color, text, txt_size, txt_color):
        self.w = w
        self.h = h
        self.color = color

        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.text = pygame.font.Font(None, txt_size).render(text, True, txt_color)
    
    def draw(self, shift_x, shift_y):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))





class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__()
        self.width = width
        self.height = height
        self.anim_count = 0
        self.images = images
        self.image = pygame.transform.scale(self, images[self.anim_count], (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = x 
        self.speed = speed



    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__(x, y, width, height, speed, images)

        self.action = 'idle'
        self.animation = {
            'idle': list(range(4)),
            'right': list(range(4, 10)),
            'left': list(range(10, 16))


        }


    
