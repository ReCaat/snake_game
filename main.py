import pygame
from pygame.math import Vector2
from classes.game import Game
from classes.button import Button

# pygame setup
pygame.init()

#Screen Setup
cell_size = 40
n = 20
m = 15
screen_width = (n) * cell_size
screen_height = (m) * cell_size 

screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 36)

#time events
MOVE_EVENT = pygame.USEREVENT #Create a custom event
pygame.time.set_timer(MOVE_EVENT, 150) #Set this event to happen every 150ms
clock = pygame.time.Clock()

#menu
state = 0

play_button = Button(screen_width/2, screen_height/4, "Play")
options_button = Button(screen_width/2, 2*screen_height/4, "Options")
quit_button = Button(screen_width/2, 3*screen_height/4, "Quit")

game = Game()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or state == -1: # the user clicked X
                running = False
        
        #Menu
        if state == 0:
            screen.fill((87, 138, 52))
            bg_rect = pygame.Rect(cell_size/2, cell_size/2, screen_width - cell_size, screen_height - cell_size)
            pygame.draw.rect(screen, (162, 209, 73), bg_rect)
            play_button.draw(screen)
            state = play_button.clicked(event, state, 1)

            options_button.draw(screen)
            state = options_button.clicked(event, state, 2)

            quit_button.draw(screen)
            state = quit_button.clicked(event, state, -1)

        #Game
        if state == 1:
            if event.type == MOVE_EVENT:
                game.screen_update()

            if event.type == pygame.KEYDOWN: #can't go backwards
                if event.key == pygame.K_w and game.snake.directios[0] != Vector2(0, 1):
                    game.snake.directios[0] = Vector2(0, -1)
                elif event.key == pygame.K_a and game.snake.directios[0] != Vector2(1, 0):
                    game.snake.directios[0] = Vector2(-1, 0)
                elif event.key == pygame.K_s and game.snake.directios[0] != Vector2(0, -1):
                    game.snake.directios[0] = Vector2(0, 1)
                elif event.key == pygame.K_d and game.snake.directios[0] != Vector2(-1, 0):
                    game.snake.directios[0] = Vector2(1, 0)

            game.munch(n, m)
            if game.colision(n, m):
                running = False

            game.draw_all(screen, n, m, cell_size, font)

        #Game Over
        if state == 2:
            pass
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()