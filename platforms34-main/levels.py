from objects import *
from settings import *











level4 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "                                 l                                    ",
    "              ---                l                                    ",
    "     ---                         l                                    ",
    "                                                                      ",
    "llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",
]









level4 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                    0 ",
    "           -------        llllllllllllllllllllllllllllllllll      llll",
    "                                        =                             ",
    "  -----                                 +                             ",
    "            ------                      +                             ",
    "                                        +                             ",
    "   ------                               +                             ",
    "            --------                    +                             ",
    "                      ----              +                             ",
    "         0                    -----     +                             ",
    "                                        +                    0        ",
    "            -------------               +                             ",
    "   1                              ------+                             ",
    " --------------------------             +                             ",
    "                                        +                             ",
    "                              -------   +                             ",
    "                    --------            +                             ",
    "             -----                      +                             ",
    "------------                            +                             ",
    "                                        +                     2       ",
    "----------------------------------------------------------------------",
]








level3 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "   0                                                                  ",
    "------              1                                                 ",
    "            ------l----------------------------------------           ",
    "                  l                                                   ",
    "------            l                                                   ",
    "            ------l                                                   ",
    "                  l           ----------------------------------------",
    "------            l                                                   ",
    "            ------l                                                   ",
    "                  l----------------------------------------           ",
    "------            l                                                   ",
    "            ------l                                                   ",
    "                  l                                                   ",
    "------            l            ---------------------------------------",
    "            ------l                                                   ",
    " 0                l                                                   ",
    "------            l                                                2  ",
    "           ------ l --------------------------------------------------",
    "             =    l                                                   ",
    "----------   +    l                                                   ",
]











level2 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                     1                                ",
    "        --------------         --------                               ",
    "                                                                      ",
    " ----                                                                 ",
    "              ----                                                    ",
    "                                                                      ",
    " ------                                                               ",
    "             -----                                                    ",
    "                                        0                             ",
    "     ------              --------               -------               ",
    "                                                                      ",
    "                                                                      ",
    "                                               0         -----------  ",
    "                                                                      ",
    "                           ------            ------                   ",
    "                              =                 =                     ",
    "           ------------       +                 +                     ",
    "               =              +                 +             2       ",
    "--------       +              +                 +        ---------    ",
]














level1 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                  ------------------                                  ",
    "                                                                      ",
    "       2                                                              ",
    "     ------                                                           ",
    "                        0                                             ",
    "                    ---------                                         ",
    "       1                                  --------                    ",
    "     --------                                                         ",
    "                                                                      ",
    "                                                        -------       ",
    "                                               0           =          ",
    "                                                           +          ",
    "                      --------------------------           +          ",
    "                            =            =                 +          ",
    "           ------           +            +                 +          ",
    "             =              +            +                 +          ",
    "----------   +              +            +                 +          ",
]


level1_width = len(level1[0])*100
level1_hight = len(level1)*30

level2_width = len(level1[0])*100
level2_hight = len(level1)*30

level_objects = pygame.sprite.Group()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft) 
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera

    l = min(0, l)
    l = max(-(camera.width - W), l)
    t = max(-(camera.height - H), t)

    return pygame.Rect(l, t, w, h)

camera = Camera(camera_config, level1_width, level1_hight)


def draw_level(level: list):


    x = y = 0     
    for row in level:
        for symbol in row:
            if symbol == "-":
                platform = MapObject(x, y, 100, 30, platform_image)
                level_objects.add(platform)
                platforms.add(platform)
            if symbol == "0":
                coin = MapObject(x, y, 100, 30, coin_image)
                level_objects.add(coin)
                coins.add(coin)

            if symbol == "1":
                key = MapObject(x, y, 100, 30, key_image)
                level_objects.add(key)

            if symbol == "2":
                chest = MapObject(x, y, 100, 30, chest_image)
                level_objects.add(chest)

























            if symbol == "=":
                platform = MapObject(x, y, 100, 30, kolona_image)
                level_objects.add(platform)
                platforms.add(platform)


            if symbol == "+":
                platform = MapObject(x, y, 100, 30, kolona_werx_image)
                level_objects.add(platform)
                platforms.add(platform)

            if symbol == "l":
                platform = MapObject(x, y, 100, 30, kirpihnau_stena)
                level_objects.add(platform)
                platforms.add(platform)



























            x += 100
        x = 0
        y += 30


    return level_objects, key, chest






