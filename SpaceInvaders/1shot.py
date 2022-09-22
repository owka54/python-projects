# Space Invaders game

import pygame
from pygame import mixer

import random
import math

# Initialize the pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("images/background.jpg")

# Background sound
mixer.music.load("sounds/background.wav")
mixer.music.play(-1)

# Title and Icon of the window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load("images/player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerimg, (x, y))

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = 40
num_of_enemies = 6
enemyBulletImg = pygame.image.load("images/bomb.png")
enemyBulletX = 250
enemyBulletY = 100
enemyBulletY_change = 0.5
enemyBullet_state = "ready"

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("images/enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))



# Bullet
bulletimg = pygame.image.load("images/laser.png")
bulletX = 0
bulletY = 480
bulletY_change = 1
# Ready - Can't see bullet on the screen
# Fire - The bullet is currently moving
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font("fonts/font1.ttf", 32)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 0))
    temp_surface = pygame.Surface(score.get_size())
    temp_surface.fill((0, 0, 0))
    temp_surface.blit(score, (0, 0))
    screen.blit(temp_surface, (x, y))

# Game over text
over_font = pygame.font.Font("fonts/font2.ttf", 128)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    banner = pygame.Surface((800, 200))
    banner.fill((0, 0, 0))
    banner.blit(over_text, (175, 250))
    screen.blit(banner, (0, 200))
    screen.blit(over_text, (175, 250))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def enemy_fire(x, y):
    global enemyBullet_state
    enemyBullet_state = "fire"
    screen.blit(enemyBulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

    

# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 64))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check weather is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.6
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.6
            if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("sounds/laser.wav")
                    bullet_sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_TAB:
                if enemyBullet_state == "ready":
                    enemy_fire(400, 100)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    # Checking the boundries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736
    
    # Enemy movement
    for i in range(num_of_enemies):

        # Game over
        dead = isCollision(playerX, playerY, enemyBulletX, enemyBulletY)
        if enemyY[i] > 440 or dead:
            enemyBulletY = 1000
            enemyBullet_state = ""
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            playerY = 2000
            game_over_text()
            mixer.music.pause()
            break
            


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change

        elif enemyX[i] >= 736:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("sounds/explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150) 

        enemy(enemyX[i], enemyY[i], i)

        

        if enemyBullet_state == "ready":
            enemyBulletX = enemyX[i]
            enemyBulletY = enemyY[i]


        x = random.randint(1, 5000)

        if score_value >= 10:
            x = random.randint(1, 2500)
            enemyBulletY_change = 0.85
            for i in range(num_of_enemies):
                if enemyX_change[i] < 0:
                    enemyX_change[i] = -0.35
                else: 
                    enemyX_change[i] = 0.35

        elif score_value >= 25:
            x = random.randint(1, 1000)
            enemyBulletY_change = 1
            for i in range(num_of_enemies):
                if enemyX_change[i] < 0:
                    enemyX_change[i] = -0.4
                else: 
                    enemyX_change[i] = 0.4
        
        elif score_value >= 50:
            x = random.randint(1, 750)
            enemyBulletY_change = 1
            for i in range(num_of_enemies):
                if enemyX_change[i] < 0:
                    enemyX_change[i] = -0.5
                else:
                    enemyX_change[i] = 0.5

        elif score_value >= 75:
            x = random.randint(1, 500)
            enemyBulletY_change = 1
            for i in range(num_of_enemies):
                if enemyX_change[i] < 0:
                    enemyX_change[i] = -0.6
                else:
                    enemyX_change[i] = 0.6

        elif score_value >= 100:
            x = random.randint(1, 350)
            enemyBulletY_change = 1
            for i in range(num_of_enemies):
                if enemyX_change[i] < 0:
                    enemyX_change[i] = -0.7
                else:
                    enemyX_change[i] = 0.7

            
        if x == 32:
            enemy_fire(enemyBulletX, enemyBulletY)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Enemy bullet movement
    if enemyBullet_state == "fire":
        enemyBulletY += enemyBulletY_change
        enemy_fire(enemyBulletX, enemyBulletY)

    if enemyBulletY >= 600:
        enemyBulletY = 100
        enemyBullet_state = "ready"
          

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
