import pygame
import random
from pygame.locals import *

# screen size 
WINDOW_W = 840
WINDOW_H = 650
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
score = 0

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game")

# www.pngaaa.com
gameDisplay = pygame.display.set_mode((WINDOW_W, WINDOW_H))
car_image = pygame.image.load("car.png")
enemy_car = pygame.image.load("enemy.car.png")
car_image = pygame.transform.scale(car_image, (200, 136)) 
white = (255, 255, 255)
velocity = 0 

#Load images and set image sizes
backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (840, 650))
gameDisplay.blit(backgroundImage, (0, 0))


def quitgame():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

clock = pygame.time.Clock()

backgroundx = 0
backgroundy = 0

enemy_car_x = 150
enemy_car_y = -150

car_x = WINDOW_W /2 - 102
car_y = WINDOW_H - 140

x_step = 8.2

play = True

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score:', True, (255, 255, 255))
screen.blit(textsurface,(10,20))
time = 0

while play:
  if car_x >= 577 or car_x <= 70 :
    play = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    car_x -= x_step
  if keys[pygame.K_RIGHT]:
    car_x += x_step
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    # if event.type == KEYDOWN:
    #   if event.key == K_UP:
    #      velocity = 5
  
  # if keys[pygame.K_UP]:
  #   velocity = 5
  
  # backgroundy = backgroundy + velocity
  # if backgroundy == 600:
  #       backgroundy = 0
       
  
  enemy_car_y = enemy_car_y + velocity
  if enemy_car_y == 700:
        enemy_car_y = -300
        enemy_car_x = random.randint(150,500)
        
   
  
  pygame.draw.line(screen, (255,255,255), (133, 0), (133,650), 4)

  textsurface = myfont.render('Score:'+str(score), True, (255, 255, 255))
  screen.blit(textsurface,(10,20))
  screen.blit(backgroundImage, [backgroundx, backgroundy - 600])
  screen.blit(backgroundImage, [backgroundx, backgroundy])
  screen.blit(enemy_car, [enemy_car_x, enemy_car_y - (800)])
  screen.blit(enemy_car, [enemy_car_x, enemy_car_y])
  screen.blit(car_image,(car_x,car_y)) 
  
  pygame.display.flip()


  clock.tick(45)

pygame.quit()

