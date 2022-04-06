import pygame
import random
from pygame.locals import *

# screen size 
WINDOW_W = 840
WINDOW_H = 650
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
score = 0

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game")

# www.pngaaa.com
bk_image = pygame.image.load("background.png")
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (200, 136)) 
white = (255, 255, 255)
velocity = 0 

clock = pygame.time.Clock()

backgroundx = 0
backgroundy = 0

# enemy_car_x = random.randint(70,577)
# enemy_car_y = 0

car_x = WINDOW_W /2 - 102
car_y = WINDOW_H - 140

x_step = 8.2

play = True

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score:', True, (255, 255, 255))
screen.blit(textsurface,(10,20))
time = 0

while play:

  screen.blit(bk_image,(0,0))
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
    if event.type == KEYDOWN:
      if event.key == K_UP:
         velocity = 5
  
  if keys[pygame.K_UP]:
    velocity = 5
  
  backgroundy = backgroundy + velocity
  if backgroundy == 600:
        backgroundy = 0
  
  # enemy_car_y = enemy_car_y + velocity
  # if enemy_car_y == 600:
  #       enemy_car_y = 0
   
  
  pygame.draw.line(screen, (255,255,255), (133, 0), (133,650), 4)

  textsurface = myfont.render('Score:'+str(score), True, (255, 255, 255))
  screen.blit(textsurface,(10,20))
  screen.blit(bk_image, [backgroundx, backgroundy - 600])
  screen.blit(bk_image, [backgroundx, backgroundy])
  # screen.blit(bk_image, [backgroundx, backgroundy - 600])
  # screen.blit(bk_image, [backgroundx, backgroundy])
  screen.blit(car_image,(car_x,car_y)) 
  
  pygame.display.flip()


  clock.tick(45)

pygame.quit()

