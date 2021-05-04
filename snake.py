import pygame

class Snake:

    def __init__(self, width, height, display, diffculity):
        self.w = 12
        self.h = 12
        self.x = width / 2
        self.y = height / 2
        self.name = 'Hossein'
        self.color = (255, 0, 0)
        self.speed = 1.5 * diffculity
        self.score = 0
        self.display = display
        self.x_change = 0
        self.y_change = 1
        self.alive = True
        self.body = []

    def show(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.w, self.h])

        for i in range(len(self.body)):
            pygame.draw.rect(self.display, self.color, [self.x + -i * self.w *self.x_change , self.y + i * self.h * self.y_change, self.w-2, self.h-2])
    
    def move(self, fruit):
        if self.x_change == -1:
            self.x -= self.speed
        elif self.x_change == 1:
            self.x += self.speed
        if self.y_change == -1:
            self.y += self.speed
        elif self.y_change == 1:
            self.y -= self.speed

        self.check_next_move(fruit)
        
    def check_next_move(self, fruit):
        #check is fruit
        if (fruit.x - fruit.r <= self.x + self.w and self.x - self.w <= fruit.x + fruit.r) and (fruit.y - fruit.r <= self.y + self.h and self.y - self.h <= fruit.y + fruit.r):
            self.score += fruit.point
            print('SCORE ->>>>>', self.score)
            self.body.append(True)
            fruit.recreate(self)
        #check is wall
        #Speed Here Means Difficulity
        if self.speed / 1.5 == 1:
            if (self.x < 0):
                self.x = self.display.get_width()
            elif (self.x > self.display.get_width() ):
                self.x = 0
            elif (self.y < 0):
                self.y = self.display.get_height()
            elif (self.y > self.display.get_height() ):
                self.y = 0
        else:
            if(self.x < 0 or self.x > self.display.get_width() or self.y > (self.display.get_height()) or self.y < 0 ):
                self.alive = False

