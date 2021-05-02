import pygame

class Snake:

    def __init__(self, width, height, d):
        self.w = 16
        self.h = 16
        self.x = width / 2
        self.y = height / 2
        self.name = 'Hossein'
        self.color = (0, 127, 0)
        self.speed = 5
        self.score = 0
        self.d = d
        self.x_change = 0
        self.y_change = 0

    def show(self):
        pygame.draw.rect(self.d, self.color, [self.x, self.y, self.w, self.h])
    
    def move(self):
        if self.x_change == -1:
            self.x -= self.speed
        elif self.x_change == 1:
            self.x += self.speed
        if self.y_change == -1:
            self.y -= self.speed
        elif self.y_change == 1:
            self.y += self.speed