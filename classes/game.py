import pygame
from classes.snake import Snake
from classes.fruit import Fruit


class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.points = 0

    def screen_update(self):
        self.snake.move()
    
    def munch(self, n, m):
        if(self.snake.body[0] == self.fruit.pos):
              self.points += 1
              self.snake.grow()
              self.fruit.new_position(self.snake.body, n, m)

    def colision(self, n, m):
        if self.snake.body[0] in self.snake.body[1:]: #with own body
            return True
        
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= n  or self.snake.body[0].y < 0 or self.snake.body[0].y >= m: #with the walls
            return True  

        return False

    def show_points(self, screen, font):
        score_surface = font.render(f'Score: {self.points}', True, (0, 0, 0))
        screen.blit(score_surface, (10, 10))

    def draw_grass(self, screen, n, m, cell):
        screen.fill((162, 209, 73))
        for i in range(n):
            for j in range(m):
                grass = pygame.Rect(i*cell, j*cell, cell, cell)
                if (i % 2 and j % 2) or (i % 2 == 0 and j % 2 == 0):
                    pygame.draw.rect(screen, (170, 215, 81), grass)

    def draw_all(self, screen, n, m, cell, font):
        self.draw_grass(screen, n, m, cell)
        self.snake.draw(screen, cell)
        self.fruit.draw(screen, cell)
        self.show_points(screen, font)
