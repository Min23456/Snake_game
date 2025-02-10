import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 800
height = 600

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game variables
snake_block = 10
snake_speed = 15

# Font styles
font_style = pygame.font.Font(None, 25)
score_font = pygame.font.Font(None, 35)

# Create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
    

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])


def gameloop():
    
    
    
    game_over = False
    
    game_close = False
    
    
    
    x1 = width / 2
    
    y1 = height / 2
    
    x1_change = 0
    
    y1_change = 0
    
    
    
    
    
    snake_list = []
    
    
    length_of_snake = 1
    
    
    foodx = round (random.randrange(0, width - snake_block) / 10.0) * 10.0
    
    foody = round (random.randrange(0, height - snake_block) / 10.0) * 10.0
    
    
    
    
    
    
    while not game_over:
        while game_close:
            screen.fill(blue)
            message("You Lost, press Q to quit or C to try again.",red)
            
            your_score(length_of_snake - 1)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        
                        game_close = False
                        
                    if event.key == pygame.K_c:
                        gameloop()
                        
                        
                        
                        
                        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                game_over = True
                
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    
                    x1_change = -snake_block
                    
                    y1_change = 0
                    
                if event.key == pygame.K_RIGHT:
                    
                    x1_change = snake_block 
                    
                    y1_change = 0
                    
                if event.key == pygame.K_UP:
                    
                    x1_change = 0
                    
                    y1_change = -snake_block
                    
                    
                    
                if event.key == pygame.K_DOWN:
                    
                    x1_change = 0
                    
                    y1_change = snake_block
                    
                
        if x1 >= width or x1 <0 or y1>= height or y1 < 0:
            game_close = True
            
        x1 += x1_change
        
        y1 += y1_change
        
        screen.fill(blue)
        
        
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        
        
        snake_head = []
        
        snake_head.append(x1)
        
        snake_head.append(y1)
        
        snake_list.append(snake_head)
        
        
        if len(snake_list) > length_of_snake:
            
            del snake_list[0]
        
            
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        
    
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            
            length_of_snake += 1
            
            
        
        clock.tick(snake_speed)
    
  
     
     
    pygame.quit()
    quit()
     
     
     
     
gameloop()


    
    






