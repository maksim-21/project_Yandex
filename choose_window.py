# Images from https://opengameart.org/content/space-shooter-redux" (by Kenney.nl)
import os
import random
import sys

import pygame

pygame.init()
pygame.display.set_caption('Star Fighter')
size = width, height = 650, 675
screen = pygame.display.set_mode(size)

FPS = 50


class Choose:

    def __init__(self, stars):
        self.stars = stars

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        intro_text = ["[A]      [F]", "",
                      "[S]      [G]", "",
                      "[D]      [H]", ""]
        rights = ["Выберите космический корабль,", "которым вы будете управлять",
                  "Images made by Kenney.nl"]

        font = pygame.font.Font('data/text.ttf', 70)
        font_ = pygame.font.Font('data/text.ttf', 35)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        for line in rights:
            string_rendered = font_.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    pass
            pygame.display.flip()
            clock.tick(FPS)

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    all_sprites = pygame.sprite.Group()
    red_plane_A = pygame.sprite.Sprite()
    red_plane_A.image = load_image("playerShip1_red.png")
    red_plane_A.rect = red_plane_A.image.get_rect()
    all_sprites.add(red_plane_A)
    red_plane_A.rect.x = 120
    red_plane_A.rect.y = 50
    blue_plane_S = pygame.sprite.Sprite()
    blue_plane_S.image = load_image("playerShip2_blue.png")
    blue_plane_S.rect = blue_plane_S.image.get_rect()
    all_sprites.add(blue_plane_S)
    blue_plane_S.rect.x = 120
    blue_plane_S.rect.y = 210
    green_plane_D = pygame.sprite.Sprite()
    green_plane_D.image = load_image("playerShip3_green.png")
    green_plane_D.rect = green_plane_D.image.get_rect()
    all_sprites.add(green_plane_D)
    green_plane_D.rect.x = 120
    green_plane_D.rect.y = 370
    green_plane_second_version_F = pygame.sprite.Sprite()
    green_plane_second_version_F.image = load_image("playerShip1_green.png")
    green_plane_second_version_F.rect = green_plane_second_version_F.image.get_rect()
    all_sprites.add(green_plane_second_version_F)
    green_plane_second_version_F.rect.x = 480
    green_plane_second_version_F.rect.y = 50
    blue_plane_second_version_G = pygame.sprite.Sprite()
    blue_plane_second_version_G.image = load_image("playerShip2_orange.png")
    blue_plane_second_version_G.rect = blue_plane_second_version_G.image.get_rect()
    all_sprites.add(blue_plane_second_version_G)
    blue_plane_second_version_G.rect.x = 480
    blue_plane_second_version_G.rect.y = 210
    red_plane_second_version_H = pygame.sprite.Sprite()
    red_plane_second_version_H.image = load_image("playerShip3_red.png")
    red_plane_second_version_H.rect = red_plane_second_version_H.image.get_rect()
    all_sprites.add(red_plane_second_version_H)
    red_plane_second_version_H.rect.x = 480
    red_plane_second_version_H.rect.y = 370

    def stars_(self):
        return self.stars

    running = True
    while running:
        for i in range(5000):
            screen.fill(pygame.Color('white'),
                        (stars_()[i][0],
                         stars_()[i][1], 1, 1))
        all_sprites.draw(screen)
        start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            all_sprites.draw(screen)
            all_sprites.update(event)
            pygame.display.flip()
    pygame.quit()
