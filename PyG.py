from numpy.lib.function_base import delete
import pygame
from sys import exit
import time
import random

pygame.init()
screen = pygame.display.set_mode((800, 450))
sky_texture = pygame.image.load('C:/assets/sky_texture.jpg')                     #loading day sky
night_sky_texture = pygame.image.load('C:/assets/night_sky_texture.jpg')         #loading night sky
pygame.display.set_caption('Godzilla vs Mike')
font_one = pygame.font.Font('C:/assets/pixel_font.ttf', 50)                       #initializing new pixel font
fps_font = pygame.font.Font('C:/assets/pixel_font.ttf', 20)                       #initializing pixel font for fps font
font_two = pygame.font.Font('C:/assets/pixel_font.ttf', 20)                       #initializing new pixel fon
ground_texture = pygame.image.load('C:/assets/brick_texture.jpg')                 #loading ground texture
sky_texture = pygame.image.load('C:/assets/sky_texture.jpg')                      #loading sky texture
bullet_texture = pygame.Surface((5,5))
bullet_texture.fill('Red')
monster_right = pygame.image.load('C:/assets/godzilla_right.png')                 #loading texture of monster right
monster_left = pygame.image.load('C:/assets/godzilla_left.png')                   #loading texture of monster left
hero_left = pygame.image.load('C:/assets/pixel_hero_left.png')
hero_right = pygame.image.load('C:/assets/pixel_hero_right.png')
text_texture = font_two.render('press w for day mode & n for night mode', True, 'White')               #finalizing text to display

texture = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                                                  #exit button
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                texture = sky_texture
                break
            if event.key == pygame.K_s:
                texture = night_sky_texture
                break
    screen.blit(text_texture, (230,50))
    if (texture):
        break
    pygame.display.update()

bulletx_left = []
bulletx_right = []

def fps():
        fps = "FPS: " + str(int(clock.get_fps()))
        return fps                                                                                     #fps counter

def fire():
    if hero == hero_right:
        bulletx_right.append(380)
    else:
        bulletx_left.append(380)
    
monster_left_pos = random.randint(801, 1200)                                                           #Monster position
monster_right_pos = -1*(random.randint(1, 400))

clock = pygame.time.Clock()                                                                            #storing fps

border = pygame.Surface((800,5))                                                                       #creating dirt on ground
border.fill('Brown')                                                                                   #coloring dirt

if (texture == sky_texture):
    text_texture = font_one.render('Game Start', True, 'Black')                                            #finalizing text to display
else:
    text_texture = font_one.render('Game Start', True, 'White')

hero = hero_right
deletel = 0
deleter = 0
while True:                                                                                            #starting our game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                                                  #exit button
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hero = hero_left
            if event.key == pygame.K_d:
                hero = hero_right

    if event.type == pygame.MOUSEBUTTONDOWN:
        if (len(bulletx_right)==0 or bulletx_right[len(bulletx_right)-1] >= 630) and hero == hero_right:
            fire()
            print (len(bulletx_right))
        elif (len(bulletx_left)==0 or bulletx_left[len(bulletx_left)-1] <= 130) and hero == hero_left:
            fire()
    if (texture == sky_texture):
        fps_update = fps_font.render(fps(), True, 'Black')
    else:
        fps_update = fps_font.render(fps(), True, 'White')
    screen.blit(ground_texture,(0,320))
    screen.blit(texture,(0,0))
    screen.blit(border,(0,360))
    screen.blit(monster_left, (monster_left_pos,298))
    screen.blit(monster_right, (monster_right_pos,298))
    screen.blit(hero, (380,325))
    screen.blit(fps_update, (0,0))
    
    for i in range(len(bulletx_left)):
        try:
            if int(bulletx_left[i]) <= int(monster_right_pos)+50:
                monster_right_pos = -1*(random.randint(1, 400))
                bulletx_left.pop(0)
                i-=1
            else:
                bulletx_left[i] = bulletx_left[i]-3
                screen.blit(bullet_texture, (bulletx_left[i], 343))
        except:
            pass

    for i in range(len(bulletx_right)):
        try:
            if int(bulletx_right[i]) >= int(monster_left_pos)+30:
                monster_left_pos = 1200
                bulletx_right.pop(0)
            else:
                bulletx_right[i] = bulletx_right[i]+3
            screen.blit(bullet_texture, (bulletx_right[i], 343))
        except:
            pass

    clock.tick(200)

    if monster_left_pos == 380:
        break                                                       #position of Godzilla
    else:
        monster_left_pos = monster_left_pos-1
        screen.blit(text_texture, (300,50))
    if monster_right_pos == 330:
        break
    else:
        monster_right_pos = monster_right_pos+1
        screen.blit(text_texture, (300,50))
    pygame.display.update()

text_texture = font_one.render('You Died', True, 'Black')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                                                  #exit button
            pygame.quit()
            exit()
    screen.blit(text_texture, (300,50))
    pygame.display.update()