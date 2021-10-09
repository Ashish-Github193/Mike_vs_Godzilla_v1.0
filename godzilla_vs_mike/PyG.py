#requesting library dependencies
from numpy.lib.function_base import delete
import pygame
from sys import exit
import time
import random



#initializing game
pygame.init()


#texture dependencies
programIcon = pygame.image.load('assets/godzilla_right.png')                   #loading game icon
pygame.display.set_icon(programIcon)                                                                                    #setting icon of game
screen = pygame.display.set_mode((800, 450))                                                                            #creating screen resolution
sky_texture = pygame.image.load('assets/sky_texture.jpg')                      #loading day sky
night_sky_texture = pygame.image.load('assets/night_sky_texture_pixel.jpg')    #loading night sky
pygame.display.set_caption('Godzilla vs Mike')                                                                          #namming main screen
font_one = pygame.font.Font('assets/pixel_font.ttf', 50)                       #initializing new pixel font
fps_font = pygame.font.Font('assets/pixel_font.ttf', 20)                       #initializing pixel font for fps font
font_two = pygame.font.Font('assets/pixel_font.ttf', 20)                       #initializing new pixel fon
ground_texture = pygame.image.load('assets/brick_texture.jpg')                 #loading ground texture
night_ground_texture = pygame.image.load('assets/night_brick_texture.jpg')     #loading ground texture
sky_texture = pygame.image.load('assets/sky_texture.jpg')                      #loading sky texture
blood = pygame.image.load('assets/blood.png')                                  #loading blood texture
bullet_texture = pygame.Surface((5,5))                                                                                  #creating bullet texture
bullet_texture.fill('Red')                                                                                              #coloring dirt to brown
monster_right = pygame.image.load('assets/godzilla_right.png')                 #loading texture of monster right
monster_left = pygame.image.load('assets/godzilla_left.png')                   #loading texture of monster left
night_monster_left = pygame.image.load('assets/night_godzilla_left.png')       #loading night godzilla left texture
night_monster_right = pygame.image.load('assets/night_godzilla_right.png')     #night right godzilla texture
hero_left = pygame.image.load('assets/pixel_hero_left.png')                    #pixel hero left texture
hero_right = pygame.image.load('assets/pixel_hero_right.png')                  #pixel hero right texture
text_texture = font_two.render('press w for day mode & n for night mode', True, 'White')                                #finalizing text to display
text_texture_level = font_two.render('Select Level: press 1 for level 1 & 2 for level 2', True, 'White')
border = pygame.Surface((800,5))                                                                                        #creating dirt on ground


#day night and level depending variables
texture = 0
speed = 0
color = ""
title = "Game Started"
showtime = 300

#score variabele
score = 0


#day night selection loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                texture = sky_texture
                color = "black"
                ground = ground_texture
                border.fill('Brown')
                monster_r = monster_right
                monster_l = monster_left
                score_font = font_two.render(str(score), True, 'Black')
                break
            if event.key == pygame.K_s:
                ground = night_ground_texture
                texture = night_sky_texture
                color = "white"
                border.fill('Black')
                monster_r = night_monster_right
                monster_l = night_monster_left
                score_font = font_two.render(str(score), True, 'Black')
                break
    screen.blit(text_texture, (230,50))
    if (texture):
        break
    pygame.display.update()


screen.fill (pygame.Color('black'))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                speed = 1
                break
            if event.key == pygame.K_2:
                speed = 2
                break
            if event.key == pygame.K_3:
                speed = 3
                break
    screen.blit(text_texture_level, (230,50))
    if (speed!=0):
        break
    pygame.display.update()

# bullets and kill lists
bulletx_left = []
bulletx_right = []
kill = []

#fps counting and returning as string
def fps():
        fps = "FPS: " + str(int(clock.get_fps()))
        return fps


#defining fire function
def fire():
    if hero == hero_right:
        bulletx_right.append(380)
    else:
        bulletx_left.append(380)


#monster position
monster_left_pos = random.randint(801, 1200)
monster_right_pos = -1*(random.randint(1, 400))


# frames per second
clock = pygame.time.Clock()
hero = hero_right
deletel = 0
deleter = 0


#starting main game
while True:
    # checking clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # direction of hero
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hero = hero_left
            if event.key == pygame.K_d:
                hero = hero_right


    # checking clicks and calling fire
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (len(bulletx_right)==0 or bulletx_right[len(bulletx_right)-1] >= 630) and hero == hero_right:
            fire()
        elif (len(bulletx_left)==0 or bulletx_left[len(bulletx_left)-1] <= 130) and hero == hero_left:
            fire()

    text_texture = font_one.render(title, True, color)

    if (texture == sky_texture):
        fps_update = fps_font.render(fps(), True, 'Black')
        score_var = "score: " + str(score)
        score_update = font_two.render(score_var, True, 'Black')
    else:
        fps_update = fps_font.render(fps(), True, 'White')
        score_var = "score: " + str(score)
        score_update = font_two.render(score_var, True, 'White')


    # displaying entities
    screen.blit(ground,(0,320))
    screen.blit(texture,(0,0))
    screen.blit(monster_l, (monster_left_pos,298))
    screen.blit(monster_r, (monster_right_pos,298))
    screen.blit(hero, (380,325))
    screen.blit(border, (0,360))
    screen.blit(fps_update, (735,0))
    screen.blit(score_update, (0,0))
    
    

    # death of right monster, bullet movement and clearing old bullets
    for i in range(len(bulletx_left)):
        try:
            if int(bulletx_left[i]) <= int(monster_right_pos)+50:
                kill.append([monster_right_pos, 500])
                monster_right_pos = -1*(random.randint(1, 400))
                bulletx_left.pop(0)
                score += 5
            else:
                bulletx_left[i] = bulletx_left[i]-3
                screen.blit(bullet_texture, (bulletx_left[i], 338))
        except:
            pass


    # death of left monster, bullet movement and clearing old bullets
    for i in range(len(bulletx_right)):
        try:
            if int(bulletx_right[i]) >= int(monster_left_pos)+30:
                kill.append([monster_left_pos, 500])
                monster_left_pos = 1200
                bulletx_right.pop(0)
                score += 5
            else:
                bulletx_right[i] = bulletx_right[i]+3
                screen.blit(bullet_texture, (bulletx_right[i], 338))
        except:
            pass


    # making Frames
    clock.tick(200)


# storing x co-ordinate of monster at the time of death
    for i in kill:
        if i[1] == 0:
            kill.pop(kill.index(i))
        else:
            i[1]-=1
            screen.blit(blood, (i[0], 360))

    
    

    # termination of game and movement of godzilla
    if monster_left_pos <= 380:
        break                                                                                                           
    else:
        monster_left_pos = monster_left_pos-speed

    if monster_right_pos >= 325:
        break
    else:
        monster_right_pos = monster_right_pos+speed
        
    screen.blit(text_texture, (300,50))
    if showtime==0:
        title=""
    else:
        showtime-=1
    print(showtime)
    pygame.display.update()


# after death
ad = pygame.Surface((100,800))                                                                                  #creating bullet texture
ad.fill('Black')
text_texture = font_one.render('You Died', True, 'Black')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit
    screen.blit(text_texture, (300,50))
    pygame.display.update()