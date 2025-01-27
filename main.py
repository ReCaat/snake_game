import pygame
from pygame.math import Vector2
from classes.game import Game

# pygame setup
pygame.init()
#Screen Setup
cell = 40
n = 20
m = 15
screen_width = (n) * cell
screen_height = (m) * cell 

screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 36)

MOVE_EVENT = pygame.USEREVENT #Create a custom event
pygame.time.set_timer(MOVE_EVENT, 150) #Set this event to happen every 200ms
clock = pygame.time.Clock()



game = Game()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # the user clicked X
            running = False
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

    game.draw_all(screen, n, m, cell, font)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()