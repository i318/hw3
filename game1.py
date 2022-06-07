import pygame
import os



WIDTH,HEIGHT = 1800, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shania's Game")

BORDER = pygame.Rect(0, 450, WIDTH,10)
MAX_BULLETS = 10
#colours
BLACK = (0,0,0)
WHITE = (255, 255, 255)
idkcolour = (255,182,193)
RED = (255,0,0)
YELLOW = (255,255,0)

red_bullets = []
yellow_bullets = []




FPS = 30

#modifying the images itself
kumaheight, kumawidth = 300, 200

rilakkuma = pygame.image.load(os.path.join('Assets', 'rill1.png'))
kuma1 = pygame.transform.scale(rilakkuma, (kumaheight, kumawidth))
strawb1 = pygame.image.load(os.path.join('assets', 'strawb.gif'))
strawbu = pygame.transform.scale(strawb1,(100, 100))

korilakkuma = pygame.image.load(os.path.join('Assets', 'ko2.png'))

#defining functions
#no need to change anything here
def red_handle_movement(keys_pressed,red):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and red.x - VEL > 0: #left
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL < 1525:  #right
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > (HEIGHT/2):
        red.y -= VEL 
    if keys_pressed[pygame.K_s] and red.y + VEL < 710:
        red.y += VEL

#no need to change anything here 
def yellow_handle_movement(keys_pressed,yellow):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > 0: 
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x - VEL < 1525: 
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: 
        yellow.y -= VEL 
    if keys_pressed[pygame.K_DOWN] and yellow.y - VEL < 220: 
        yellow.y += VEL



def add_bg():
    bg = pygame.image.load(os.path.join('Assets', 'strawberry.jpg'))
    

def draw_window(red,yellow, red_bullets, yellow_bullets):
    WIN.fill((idkcolour))
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(kuma1, (red.x, red.y))
    WIN.blit(korilakkuma, (yellow.x, yellow.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update()

VEL = 20
BULLET_VEL=20    

RED_HIT = pygame.USEREVENT + 1                                                                                                                                                                                                                                                                                                                                                                                                                          
YELLOW_HIT = pygame.USEREVENT + 2 

#can try switching colours, but looks right
def handle_bullets(red_bullets, yellow_bullets, red, yellow):   
        for bullet in red_bullets:
            bullet.x += BULLET_VEL
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.remove(bullet)
        for bullet in yellow_bullets:
            bullet.x -= BULLET_VEL
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow_bullets.remove(bullet)




def main():
    red = pygame.Rect(100,500, kumawidth, kumaheight)
    yellow = pygame.Rect(1200,100, kumawidth, kumaheight)
    red_bullets = []
    yellow_bullets = []

#something wrong here for sure

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x, yellow.y + yellow.height//2 - 2 , 10, 5)
                    yellow_bullets.append(bullet)
        #print(red_bullets, yellow_bullets)
   




        keys_pressed = pygame.key.get_pressed()
#key controls 

        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red,yellow,red_bullets,yellow_bullets)
        ##draw_window(yellow,red,red_bullets,yellow_bullets) <- caused error


    pygame.quit()

    




#running the program

if __name__ == "__main__":
    main()