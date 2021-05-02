import snake
import pygame
import os

if __name__ == '__main__':
    os.system('cls||clear')
    width = 400
    height = 300

    display = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()

    snake = snake.Snake(width, height, display)   

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    snake.x_change = -1
                    snake.y_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    snake.x_change = 1
                    snake.y_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    snake.x_change = 0
                    snake.y_change = 1
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    snake.x_change = 0
                    snake.y_change = -1
        snake.move()
        snake.show()

        display.fill((0, 255, 0))
        pygame.display.update()
        clock.tick(60)