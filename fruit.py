import pygame
import random


class Fruit:
    def __init__(self, width, height, display, snake):
        self.r = 10
        self.display = display
        self.width = width
        self.height = height
        self.point = 1
        self.recreated = 0
        self.x = 0
        self.y = 0
        self.recreate(snake)

    def show(self):
        if self.r == 10:
            self.display.blit(pygame.image.load('assets/img/apple.png'), (self.x, self.y))
        else:
            self.display.blit(pygame.image.load('assets/img/apple_big.png'), (self.x, self.y))

    def recreate(self, snake):
        self.recreated += 1

        while True:
            valid_position = True
            self.x = random.randint(0, self.width - 30)
            self.y = random.randint(0, self.height - 30)
            if (snake.x == self.x) and (snake.y == self.y):
                continue
            for i in range(len(snake.body)):
                if (snake.body[i].x == self.x) and (snake.body[i].y == self.y):
                    valid_position = False
                    break
            if valid_position:
                break

        if self.recreated % 5 == 0:
            self.point = 3
            self.r = 20
        else:
            self.point = 1
            self.r = 10
