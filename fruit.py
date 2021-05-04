import pygame
import random

class Fruit:
    def __init__(self, width, height, display, snake):
        self.r = 10
        self.display = display
        self.color = (0, 127,0)
        self.width = width
        self.height = height
        self.point = 1
        self.recreated = 0
        self.x = 0
        self.y = 0
        self.recreate(snake)

    def show(self):
        pygame.draw.circle(self.display, self.color, [self.x, self.y], self.r)
        
    def recreate(self, snake):
        self.recreated += 1

        if (self.recreated % 5 == 0):
            while True:
                self.x = random.randint(0, self.width - 20)
                if snake.x != self.x: break
            while True:
                self.y = random.randint(0, self.height - 20)
                if snake.y != self.y: break
            self.point = 3
            self.r = 20
        else: 
            while True:
                self.x = random.randint(0, self.width - 10)
                if snake.x != self.x: break
            while True:
                self.y = random.randint(0, self.height - 10)
                if snake.y != self.y: break
            self.point = 1
            self.r = 10

