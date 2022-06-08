import pygame
import random
import cv2
import mediapipe as mp
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

#mediapipe
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# www.pngaaa.com
gameDisplay = pygame.display.set_mode((WINDOW_W, WINDOW_H))
car_image = pygame.image.load("car.png")
enemy_car = pygame.image.load("enemy.car.png")
car_image = pygame.transform.scale(car_image, (200, 136)) 
velocity = 0 

#Load images and set image sizes
backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (840, 650))
gameDisplay.blit(backgroundImage, (0, 0))


def quitgame():
    pygame.quit()
    quit()
def bilt():
  screen.blit(textsurface,(10,20))
  screen.blit(backgroundImage, [backgroundx, backgroundy - 600])
  screen.blit(backgroundImage, [backgroundx, backgroundy])
  screen.blit(enemy_car, [enemy_car_x, enemy_car_y - (800)])
  screen.blit(enemy_car, [enemy_car_x, enemy_car_y])
  screen.blit(car_image,(car_x,car_y)) 
clock = pygame.time.Clock()
def fingers():
      #credit ziv1004ri
    index_finger1_y1 = multiLandMarks[0].landmark[8].y
    index_finger1_y2 = multiLandMarks[0].landmark[5].y
    index_finger2_y1 = multiLandMarks[0].landmark[12].y
    index_finger2_y2 = multiLandMarks[0].landmark[9].y
    index_finger3_y1 = multiLandMarks[0].landmark[16].y
    index_finger3_y2 = multiLandMarks[0].landmark[13].y
    index_finger4_y1 = multiLandMarks[0].landmark[20].y
    index_finger4_y2 = multiLandMarks[0].landmark[17].y
    if index_finger1_y1 < index_finger1_y2 and index_finger2_y1 < index_finger2_y2 and index_finger3_y1 > index_finger3_y2 and index_finger4_y1 > index_finger4_y2:
      quitgame()
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
  ret, frame = cap.read(0)
  RGB_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  results = hands.process(RGB_image)
  multiLandMarks = results.multi_hand_landmarks
  if multiLandMarks:
     # go over all hands found and draw them on the BGR image
    for handLms in multiLandMarks:
      mpDraw.draw_landmarks(frame, handLms, mp_Hands.HAND_CONNECTIONS)
    index_finger_x = multiLandMarks[0].landmark[8].x
    fingers()
    if index_finger_x > 0 :
      print(index_finger_x)

    if car_x >= 577 or car_x <= 70 :
      play = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or index_finger_x < 0.33:
      car_x += x_step
    if keys[pygame.K_RIGHT] or index_finger_x > 0.66:
      car_x -= x_step
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        play = False
      if event.type == KEYDOWN:
        if event.key == K_UP or index_finger_x > 0.33 and index_finger_x < 0.66:
          velocity = 5
    
    if keys[pygame.K_UP]:
      velocity = 5
    
    backgroundy = backgroundy + velocity
    if backgroundy == 600:
          backgroundy = 0
        
    
    enemy_car_y = enemy_car_y + velocity
    if enemy_car_y == 700:
          enemy_car_y = -300
          enemy_car_x = random.randint(150,500)
    
    
    
    pygame.draw.line(screen, (255,255,255), (133, 0), (133,650), 4)

    textsurface = myfont.render('Score:'+str(score), True, (255, 255, 255))
    bring_handto_place = myfont.render('hand not in right place', True, (255, 255, 255))
    bilt()


  pygame.display.flip()


  clock.tick(45)

pygame.quit()

