import pygame, random
from pygame.math import Vector2

class Fruit:
    def __init__(self): #Aways start in the same position
        self.x = 13
        self.y = 7
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        fruit_rect = pygame.Rect(int(self.pos.x)*cell, int(self.pos.y)*cell, cell, cell)
        pygame.draw.rect(screen, (255, 90, 100), fruit_rect)
    
    def new_position(self, snake_body):
        # Try to generate a random position out of snake body
        while True:
            self.x = random.randint(0, n-1)
            self.y = random.randint(0, m-1)
            self.pos = Vector2(self.x, self.y)
            if self.pos not in snake_body: 
                break

class Snake:
    def __init__(self):
        self.directios = [Vector2(1,0), Vector2(1,0), Vector2(1,0)]
        self.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
    
    def draw(self):
        #It was the way I managed to make the snake pieces centralized, lmao
        for i, part in enumerate(self.body):
            x_pos = int(part.x)*cell + cell/2
            y_pos = int(part.y)*cell + cell/2 

            if self.directios[i] == Vector2(1, 0) or self.directios[i] == Vector2(-1, 0):  #shrink the corect side as the snake grows
                body_surface = pygame.Surface((cell, cell * (100 - i/2)/100))
            else:
                body_surface = pygame.Surface((cell * (100 - i/2)/100, cell))
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

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.points = 0

    def screen_update(self):
        self.snake.move()
    
    def munch(self):
        if(self.snake.body[0] == self.fruit.pos):
              self.points += 1
              self.snake.grow()
              self.fruit.new_position(self.snake.body)

    def colision(self):
        if self.snake.body[0] in self.snake.body[1:]: #with own body
            return True
        
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= n  or self.snake.body[0].y < 0 or self.snake.body[0].y >= m: #with the walls
            return True  

        return False

    def showPoints(self):
        score_surface = font.render(f'Score: {self.points}', True, (0, 0, 0))
        screen.blit(score_surface, (10, 10))

    def draw_grass(self):
        screen.fill((162, 209, 73))
        for i in range(n):
            for j in range(m):
                grass = pygame.Rect(i*cell, j*cell, cell, cell)
                if (i % 2 and j % 2) or (i % 2 == 0 and j % 2 == 0):
                    pygame.draw.rect(screen, (170, 215, 81), grass)

    def draw_all(self):
        self.draw_grass()
        self.snake.draw()
        self.fruit.draw()
        self.showPoints()

# pygame setup
pygame.init()
#Screen Setup
cell = 40
n = 20
m = 15
screen_width = (n) * cell
screen_hight = (m) * cell 

screen = pygame.display.set_mode((screen_width, screen_hight))
font = pygame.font.Font(None, 36)

MOVE_EVENT = pygame.USEREVENT #Create a custom event
pygame.time.set_timer(MOVE_EVENT, 150) #Set this event to happen every 200ms
clock = pygame.time.Clock()

game = Main()





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

        game.munch()
        if game.colision():
            running = False

    game.draw_all()
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()