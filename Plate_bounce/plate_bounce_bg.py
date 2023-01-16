#project and code written by Rajeev K R, github.com/Rajeev-K-R

import pygame
from pygame import mixer

#initialize pygame
pygame.init()

mixer.music.load('Assets/background.wav')
mixer.music.play(-1)
hit_sound = mixer.Sound('Assets/explosion.wav')

#create screen
screen = pygame.display.set_mode((600,600))


#title and icon
pygame.display.set_caption("Gameee")
icon = pygame.image.load('Assets/chess-piece.png')
pygame.display.set_icon(icon)


#player
playerimg = pygame.image.load('Assets/plate.png')
dotimg = pygame.image.load('Assets/dot.png')
playerx = 268
playery = 525
playerx_change = 0

dotx = 292
doty = 292
dotx_change = 0
doty_change = 6.4

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

def player(x,y):
    screen.blit(playerimg,(x,y))

def dot(x,y):
    screen.blit(dotimg,(x,y))

def show_score():
    score = font.render(str(score_value),True,(255,255,255))
    screen.blit(score,(550,20))


#game loop
running = True

while running:
    screen.blit(pygame.image.load('Assets/night_background.png'),(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -4
            if event.key == pygame.K_RIGHT:
                playerx_change = 4

            if event.key == pygame.K_RETURN:
                    dotx = 292
                    doty = 292
                    dotx_change = 0
                    doty_change = 6.4
                    playerx = 268
                    playery = 525
                    playerx_change = 0
                    score_value = 0
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    
    if doty >= 525+29-16:
        if dotx<=playerx-8 or dotx >= playerx+56:
            dotx_change = 0
            doty_change = 0
            screen.blit(pygame.image.load('Assets/game_over.png'),(236,236))

        else :
            score_value += 1
            doty_change = -doty_change
            dotx_change = (dotx+8-playerx-32)/6
            hit_sound.play()
    if dotx <= 0:
        dotx_change = -dotx_change
    if dotx >= 583:
        dotx_change = -dotx_change
    if doty <= 0:
        doty_change = -doty_change
    playerx += playerx_change
    dotx += dotx_change
    doty += doty_change
    if playerx<=0:
        playerx = 0
    elif playerx>=536:
        playerx = 536
    player(playerx,playery)
    dot(dotx,doty)
    show_score()
    pygame.display.update()
