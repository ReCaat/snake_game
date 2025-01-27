import random, pygame
from pygame.math import Vector2

class Fruit:
    def __init__(self): #Aways start in the same position
        self.x = 13
        self.y = 7
        self.pos = Vector2(self.x, self.y)

    def draw(self, screen, cell):
        fruit_rect = pygame.Rect(int(self.pos.x)*cell, int(self.pos.y)*cell, cell, cell)
        pygame.draw.rect(screen, (255, 90, 100), fruit_rect)
    
    def new_position(self, snake_body, n, m):
        # Try to generate a random position out of snake body
        while True:
            self.x = random.randint(0, n-1)
            self.y = random.randint(0, m-1)
            self.pos = Vector2(self.x, self.y)
            if self.pos not in snake_body: 
                break
