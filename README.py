import pygame

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
car_image = pygame.transform.scale(car_image, (200, 140))  

clock = pygame.time.Clock()


car_x = WINDOW_W /2 - 102
car_y = WINDOW_H - 140

x_step = 10

play = True


myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score:', True, (255, 255, 255))
screen.blit(textsurface,(10,20))


while play:
  screen.blit(bk_image,(0,0))
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    car_x -= x_step
  if keys[pygame.K_RIGHT]:
    car_x += x_step
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
          car_x -= x_step
      if event.key == pygame.K_RIGHT:
        car_x += x_step
  

  screen.blit(car_image,(car_x,car_y))
  textsurface = myfont.render('Score:'+str(score), True, (255, 255, 255))
  screen.blit(textsurface,(10,20))
 
  
  pygame.display.flip()


  clock.tick(40)

pygame.quit()

