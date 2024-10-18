import pygame 
import sys 
import random
pygame.init()
pygame.mixer.init()
# all the varible for the game 
run = True
FPS = 60
screen_width , screen_height = 390,590
clock = pygame.time.Clock()
road_img = pygame.image.load("Assets/images/road.png")
car_img = pygame.transform.scale(pygame.image.load("Assets/images/car.png"),(80,160))
obstacle2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Assets/images/obstacle2.png"),(90,160)),180)
roadlis = []
obstaclelis =[]
roadx,roady = 200,600
carx,cary = 200,500
car_speed = 4
obsx,obsy = 0,-200
score = 0
play = True
play_music = True
bg_music = pygame.mixer.music.load("Assets/music/background music.mp3")
if play_music: pygame.mixer.music.play(loops = 100)
car_music = pygame.mixer.Sound("Assets/music/car music.wav")
crash_sound  = pygame.mixer.Sound("Assets/music/crash.wav")
#  basic screen setup 
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Car Game")

# drawing road 

for i in range(100,1000 ,100):
    rect = road_img.get_rect(center = (roadx,roady-i))
    roadlis.append(rect)

def roadfunc():
    
   for road in roadlis:
       if play :road.y +=5
       if road.y > 600 :
          roadlis.pop(roadlis.index(road))
          rect = road_img.get_rect(center = (roadx,roadlis[-1].y))
          roadlis.append(rect)
       screen.blit(road_img,road)
      
# creating the car 

def carfunc():
   global car_rect
   car_rect = car_img.get_rect(center = (carx,cary))
   screen.blit(car_img,car_rect)


# creating the obsctacle part 


for i in range(0,500,250):
    obsx = random.randint(52,348) 
    obstacle_rect = obstacle2.get_rect(center = (obsx ,obsy+i))
    obstaclelis.append(obstacle_rect)
# creating the score part 
def display_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

def obstaclefunc():
    global obsx , obsy , score
    for obstacle in obstaclelis:
        obsx = random.randint(52,348) 
        if play : obstacle.y +=5
        if obstacle.y > 600:
         obstacle_rect = obstacle2.get_rect(center = (obsx ,obsy))
         obstaclelis.pop(obstaclelis.index(obstacle))
         score+=1
         obstaclelis.append(obstacle_rect)
        screen.blit(obstacle2,obstacle)

# game over text 

def display_game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, (242, 95, 10))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
#  collision and score part 

def colision():
    global play , play_music
    for obstacle in obstaclelis:
     if pygame.Rect.colliderect(obstacle , car_rect):
        play = False
        play_music = False
        crash_sound.play()
        display_game_over()
     
         

# main fuction of the game 

def main():
    global roady , carx,cary , obsx ,obsy , play_music
    while run :
     
     roadfunc()
     carfunc()
     obstaclefunc()
     colision()
     display_score(score)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and carx>52 and play:
            carx -= car_speed
            car_music.play()
     if keys[pygame.K_RIGHT] and carx<348and play:
            carx += car_speed
            car_music.play()
     clock.tick(FPS)
     pygame.display.update()
if __name__ == "__main__":
   main()