import pygame
import random
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    
    score = 0
    life = 3
    
    text_font = pygame.font.Font('VT323-Regular.ttf', 50)
    text_surface = text_font.render('Score: ' + str(score), False, 'white')
    
    player = pygame.Rect(350, 700, 100, 10)
    ball = pygame.Rect(395, 395, 10, 10)
    ball_x_speed = 0
    ball_y_speed = 6
    
    left_wall = pygame.Rect(0, 0, 10, 800)
    right_wall = pygame.Rect(790, 0, 10, 800)
    top_wall = pygame.Rect(-10, 0, 820, 10)
    
    obsO1 = pygame.Rect(23, 151, 50, 50)
    obsO2 = pygame.Rect(87, 151, 50, 50)
    obsO3 = pygame.Rect(151, 151, 50, 50)
    obsO4 = pygame.Rect(215, 151, 50, 50)
    obsO5 = pygame.Rect(279, 151, 50, 50)
    obsO6 = pygame.Rect(343, 151, 50, 50)
    obsO7 = pygame.Rect(407, 151, 50, 50)
    obsO8 = pygame.Rect(471, 151, 50, 50)
    obsO9 = pygame.Rect(535, 151, 50, 50)
    obsO10 = pygame.Rect(599, 151, 50, 50)
    obsO11 = pygame.Rect(663, 151, 50, 50)
    obsO12 = pygame.Rect(727, 151, 50, 50)
    
    obsG1 = pygame.Rect(23, 87, 50, 50)
    obsG2 = pygame.Rect(87, 87, 50, 50)
    obsG3 = pygame.Rect(151, 87, 50, 50)
    obsG4 = pygame.Rect(215, 87, 50, 50)
    obsG5 = pygame.Rect(279, 87, 50, 50)
    obsG6 = pygame.Rect(343, 87, 50, 50)
    obsG7 = pygame.Rect(407, 87, 50, 50)
    obsG8 = pygame.Rect(471, 87, 50, 50)
    obsG9 = pygame.Rect(535, 87, 50, 50)
    obsG10 = pygame.Rect(599, 87, 50, 50)
    obsG11 = pygame.Rect(663, 87, 50, 50)
    obsG12 = pygame.Rect(727, 87, 50, 50)
    
    obsB1 = pygame.Rect(23, 23, 50, 50)
    obsB2 = pygame.Rect(87, 23, 50, 50)
    obsB3 = pygame.Rect(151, 23, 50, 50)
    obsB4 = pygame.Rect(215, 23, 50, 50)
    obsB5 = pygame.Rect(279, 23, 50, 50)
    obsB6 = pygame.Rect(343, 23, 50, 50)
    obsB7 = pygame.Rect(407, 23, 50, 50)
    obsB8 = pygame.Rect(471, 23, 50, 50)
    obsB9 = pygame.Rect(535, 23, 50, 50)
    obsB10 = pygame.Rect(599, 23, 50, 50)
    obsB11 = pygame.Rect(663, 23, 50, 50)
    obsB12 = pygame.Rect(727, 23, 50, 50)
    
    heart = pygame.image.load('heart.png').convert_alpha()
    heart1_rect = heart.get_rect(topleft = (650, 740))
    heart2_rect = heart.get_rect(topleft = (690, 740))
    heart3_rect = heart.get_rect(topleft = (730, 740))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.fill((0, 0, 0))
        
        pygame.draw.rect(screen, (255, 255, 255), player)
        pygame.draw.rect(screen, ('red'), ball)
        pygame.draw.rect(screen, ('white'), left_wall)
        pygame.draw.rect(screen, ('white'), right_wall)
        pygame.draw.rect(screen, ('white'), top_wall)
        
        pygame.draw.rect(screen, ('orange'), obsO1)
        pygame.draw.rect(screen, ('orange'), obsO2)
        pygame.draw.rect(screen, ('orange'), obsO3)
        pygame.draw.rect(screen, ('orange'), obsO4)
        pygame.draw.rect(screen, ('orange'), obsO5)
        pygame.draw.rect(screen, ('orange'), obsO6)
        pygame.draw.rect(screen, ('orange'), obsO7)
        pygame.draw.rect(screen, ('orange'), obsO8)
        pygame.draw.rect(screen, ('orange'), obsO9)
        pygame.draw.rect(screen, ('orange'), obsO10)
        pygame.draw.rect(screen, ('orange'), obsO11)
        pygame.draw.rect(screen, ('orange'), obsO12)
        
        pygame.draw.rect(screen, ('green'), obsG1)
        pygame.draw.rect(screen, ('green'), obsG2)
        pygame.draw.rect(screen, ('green'), obsG3)
        pygame.draw.rect(screen, ('green'), obsG4)
        pygame.draw.rect(screen, ('green'), obsG5)
        pygame.draw.rect(screen, ('green'), obsG6)
        pygame.draw.rect(screen, ('green'), obsG7)
        pygame.draw.rect(screen, ('green'), obsG8)
        pygame.draw.rect(screen, ('green'), obsG9)
        pygame.draw.rect(screen, ('green'), obsG10)
        pygame.draw.rect(screen, ('green'), obsG11)
        pygame.draw.rect(screen, ('green'), obsG12)
        
        pygame.draw.rect(screen, ('blue'), obsB1)
        pygame.draw.rect(screen, ('blue'), obsB2)
        pygame.draw.rect(screen, ('blue'), obsB3)
        pygame.draw.rect(screen, ('blue'), obsB4)
        pygame.draw.rect(screen, ('blue'), obsB5)
        pygame.draw.rect(screen, ('blue'), obsB6)
        pygame.draw.rect(screen, ('blue'), obsB7)
        pygame.draw.rect(screen, ('blue'), obsB8)
        pygame.draw.rect(screen, ('blue'), obsB9)
        pygame.draw.rect(screen, ('blue'), obsB10)
        pygame.draw.rect(screen, ('blue'), obsB11)
        pygame.draw.rect(screen, ('blue'), obsB12)
        
        screen.blit(heart, heart1_rect)
        screen.blit(heart, heart2_rect)
        screen.blit(heart, heart3_rect)
        
        screen.blit(text_surface, (40, 740))
        text_surface = text_font.render('Score: ' + str(score), False, 'white')
        
        key = pygame.key.get_pressed()
        
        # Movement and exit
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
        if key[pygame.K_RIGHT]:
            player.right += 10
        if key[pygame.K_LEFT]:
            player.left -= 10
        if key[pygame.K_SPACE]:
            life = 3
            score = 0
            heart1_rect.top = 740
            heart2_rect.top = 740
            heart3_rect.top = 740
            ball.left = 395
            ball.top = 395
            ball_x_speed = 0
            ball_y_speed = 6
            player.left = 350
            
            obsO1.top = 151
            obsO2.top = 151
            obsO3.top = 151
            obsO4.top = 151
            obsO5.top = 151
            obsO6.top = 151
            obsO7.top = 151
            obsO8.top = 151
            obsO9.top = 151
            obsO10.top = 151
            obsO11.top = 151
            obsO12.top = 151
            
            obsG1.top = 87
            obsG2.top = 87
            obsG3.top = 87
            obsG4.top = 87
            obsG5.top = 87
            obsG6.top = 87
            obsG7.top = 87
            obsG8.top = 87
            obsG9.top = 87
            obsG10.top = 87
            obsG11.top = 87
            obsG12.top = 87
            
            obsB1.top = 23
            obsB2.top = 23
            obsB3.top = 23
            obsB4.top = 23
            obsB5.top = 23
            obsB6.top = 23
            obsB7.top = 23
            obsB8.top = 23
            obsB9.top = 23
            obsB10.top = 23
            obsB11.top = 23
            obsB12.top = 23
            
        # Collisions
        if player.colliderect(left_wall):
            if player.right > left_wall.right:
                player.right += 10
        if player.colliderect(right_wall):
            if player.left < right_wall.left:
                player.left -= 10
        if ball.colliderect(player):
            ball.top -= 10
            ball_y_speed = -ball_y_speed
            #ball_x_speed = random.randint(-6, 6)
            if ball.x < player.x + 25:
                ball_x_speed = -6
            if ball.x < player.x + 50:
                ball_x_speed = -3
            if ball.x < player.x + 75:
                ball_x_speed = 3
            else:
                ball_x_speed = 6
        if ball.colliderect(top_wall):
            ball_y_speed = -ball_y_speed
        if ball.colliderect(left_wall) or ball.colliderect(right_wall):
            ball_x_speed = -ball_x_speed
        
        if ball.colliderect(obsO1):
            obsO1.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO2):
            obsO2.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO3):
            obsO3.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO4):
            obsO4.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO5):
            obsO5.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO6):
            obsO6.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO7):
            obsO7.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO8):
            obsO8.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO9):
            obsO9.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO10):
            obsO10.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO11):
            obsO11.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsO12):
            obsO12.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
            
        if ball.colliderect(obsG1):
            obsG1.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG2):
            obsG2.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG3):
            obsG3.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG4):
            obsG4.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG5):
            obsG5.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG6):
            obsG6.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG7):
            obsG7.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG8):
            obsG8.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG9):
            obsG9.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG10):
            obsG10.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG11):
            obsG11.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsG12):
            obsG12.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
            
        if ball.colliderect(obsB1):
            obsB1.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB2):
            obsB2.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB3):
            obsB3.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB4):
            obsB4.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB5):
            obsB5.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB6):
            obsB6.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB7):
            obsB7.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB8):
            obsB8.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB9):
            obsB9.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB10):
            obsB10.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB11):
            obsB11.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
        if ball.colliderect(obsB12):
            obsB12.top = -100
            ball_x_speed = random.randint(-6, 6)
            ball_y_speed = -ball_y_speed
            score += 1
            
        ball.top += ball_y_speed
        ball.left += ball_x_speed
        if ball.top > 800:
            ball.top = 400
            ball.left = 400
            ball_x_speed = 0
            life -= 1
            if life == 2:
                heart1_rect.top = -100
            elif life == 1:
                heart2_rect.top = -100
            elif life == 0:
                heart3_rect.top = -100
                ball.top = -1000
                ball.left = -1000
                ball_x_speed = 0
                ball_y_speed = 0
        
        if score == 36:
            ball.top = -1000
            ball_x_speed = 0
            ball_y_speed = 0
        
        pygame.display.update()
        clock.tick(60)
        
        
if __name__ == "__main__":
    main()
else:
    print('!!! ERROR !!! not main file')