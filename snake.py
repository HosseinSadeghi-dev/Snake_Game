import pygame


class Snake:

    def __init__(self, width, height, display, difficulty):
        self.w = 12
        self.h = 12
        self.x = width / 2
        self.y = height / 2
        self.name = 'Hossein'
        self.color = (0, 255, 255)
        self.speed = 1.5 * difficulty
        self.score = 0
        self.display = display
        self.x_change = -1
        self.y_change = 0
        self.alive = True
        self.body = []

    def show(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.w, self.h])

        for i in range(0, len(self.body)):
            if i % 2 == 0:
                pygame.draw.rect(self.display, (0, 0, 255), [self.body[i].x, self.body[i].y, self.w, self.h])
            else:
                pygame.draw.rect(self.display, self.color, [self.body[i].x, self.body[i].y, self.w, self.h])

    def move(self, fruit):
        head_old_x = self.x
        head_old_y = self.y
        if self.x_change == -1:
            self.x -= self.speed
        elif self.x_change == 1:
            self.x += self.speed
        if self.y_change == -1:
            self.y += self.speed
        elif self.y_change == 1:
            self.y -= self.speed

        # move body if body exists
        if len(self.body) > 0:
            self.body[0].x = head_old_x
            self.body[0].y = head_old_y
            for i in range(0, len(self.body)):
                # save old positions
                if i == 0:
                    self.body[i].old_x = self.body[i].x
                    self.body[i].old_y = self.body[i].y
                else:
                    self.body[i].old_x = self.body[i].x
                    self.body[i].old_y = self.body[i].y
                # move
                if i == 0:
                    self.body[i].x = head_old_x
                    self.body[i].y = head_old_y
                else:
                    self.body[i].x = self.body[i - 1].old_x
                    self.body[i].y = self.body[i - 1].old_y

        self.check_next_move(fruit)

    def check_next_move(self, fruit):
        # check is wall
        # Speed Here Means Difficulty
        if self.speed / 1.5 == 1:
            if self.x < 0:
                self.x = self.display.get_width()
            elif self.x > self.display.get_width():
                self.x = 0
            elif self.y < 0:
                self.y = self.display.get_height()
            elif self.y > self.display.get_height():
                self.y = 0
        else:
            if self.x < 0 or self.x > self.display.get_width() or self.y > self.display.get_height() or self.y < 0:
                self.alive = False

        # check is itself
        for i in range(1, len(self.body)):
            if (self.x == self.body[i].x) and (self.y == self.body[i].y):
                self.alive = False
                break

        # check is fruit
        if (fruit.x - fruit.r <= self.x + self.w and self.x - self.w <= fruit.x + fruit.r) and (
                fruit.y - fruit.r <= self.y + self.h and self.y - self.h <= fruit.y + fruit.r) and (self.alive == True):
            self.score += fruit.point

            # add to body
            if len(self.body) == 0:
                self.body.append(Body(self.x, self.y))
            else:
                self.body.append(Body(self.body[-1].x, self.body[-1].y))

            fruit.recreate(self)


class Body:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.old_x = 0
        self.old_y = 0
