import pygame

class Button:
    def __init__(self, x, y, text="button"):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 70
        self.text = text
        self.color = (100, 100, 255)
        self.text_color = (255, 255, 255)

    def draw(self, screen):
        rect_x = self.x - self.width // 2
        rect_y = self.y - self.height // 2

        font = pygame.font.SysFont("timesnewroman", 40)
        pygame.draw.rect(screen, self.color, (rect_x, rect_y, self.width, self.height), border_radius=10)

        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=(self.x, self.y))

        screen.blit(text_surf, text_rect)

    def hovered(self):
        cursor = pygame.mouse.get_pos()
        x_borders = cursor[0] <= self.x + self.width/2 and cursor[0] >= self.x - self.width/2
        y_borders = cursor[1] <= self.y + self.height/2 and cursor[1] >= self.y - self.height/2
        if x_borders and y_borders:
            self.color = (125, 125, 255) #hover
            return True
        else:
            self.color = (100, 100, 255)
            return False
    
    def clicked(self, event, state, next_state):
        hover = self.hovered()
        if event.type == pygame.MOUSEBUTTONDOWN and hover:
            return next_state
        else:
            return state
            