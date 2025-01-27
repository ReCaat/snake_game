import pygame
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.directios = [Vector2(1,0), Vector2(1,0), Vector2(1,0)]
        self.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
    
    def draw(self, screen, cell):
        #It was the way I managed to make the snake pieces centralized, lmao
        for i, part in enumerate(self.body):
            x_pos = int(part.x)*cell + cell/2
            y_pos = int(part.y)*cell + cell/2 

            if self.directios[i] == Vector2(1, 0) or self.directios[i] == Vector2(-1, 0):  #shrink the corect side as the snake grows
                body_surface = pygame.Surface((cell, max(15, cell * (100 - i/2)/100)))
            else:
                body_surface = pygame.Surface((max(15, cell * (100 - i/2))/100, cell))
            body_surface.fill((70, 116, 233))            
            body_part = body_surface.get_rect(center = (x_pos, y_pos))
            screen.blit(body_surface, body_part)

            # body_rect = pygame.Rect(x_pos , y_pos, cell, cell)
            # pygame.draw.rect(screen, (70, 116, 233), body_rect)

    def move(self):
        new_directions = [self.directios[0]] + self.directios[:-1]
        self.directios = new_directions

        body_copy = self.body[:-1]
        body_copy.insert(0, self.body[0] + self.directios[0])
        self.body = body_copy

    def grow(self):
        self.body.append(self.body[-1])
        self.directios.append(self.directios[-1])
