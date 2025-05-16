import pygame

pygame.init()


W, H = 1280, 700
FPS = 20
coints_count = 0
is_key = False
level_count = 1

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Lumo Platformer")

clock = pygame.time.Clock()

""" ГРУПИ ОБ'ЄКТІВ """
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()


""" КАРТИНКИ СПРАЙТІВ """
bg = pygame.transform.scale(pygame.image.load("tile_0000.png"), (W, H))

platform_image = pygame.image.load("tile_0065.png")


kolona_image = pygame.image.load("tile_0221.png")


kolona_werx_image = pygame.image.load("tile_0201.png")

kirpihnau_stena = pygame.image.load("tile_0050.png")

player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png"),
]

chest_image = pygame.image.load("tile_0389.png")
coin_image = pygame.image.load("tile_0002.png")
key_image = pygame.image.load("tile_0096.png")
portal_image = pygame.image.load("png-klev-club-yils-p-pikselnii-p.png")


""" ШРИФТИ """
pygame.font.init()
font1 = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 80)
font3 = pygame.font.SysFont(None, 160, bold=True)


""" ТЕКСТИ """
find_key_txt = font2.render("Знайди ключ!", True, (255, 255, 255))
open_chest_txt = font2.render("Натисни e щоб відкрити!", True, (255, 255, 255))
get_key_txt = font2.render("Натисни e щоб підібрати!", True, (255, 255, 255))
game_name = font3.render("Lumo Adventure", True, (255, 255, 255))
