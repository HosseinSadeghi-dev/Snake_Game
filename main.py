import snake
import pygame
import os

if __name__ == '__main__':
    os.system('cls||clear')
    width = 600
    height = 500

    window = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    print('display in main', window)

    s = snake.Snake(width, height, window)   

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    s.x_change = -1
                    s.y_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    s.x_change = 1
                    s.y_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    s.x_change = 0
                    s.y_change = 1
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    s.x_change = 0
                    s.y_change = -1
        s.move()

        window.fill((0, 255, 0))
        pygame.display.update()
        s.show()
        clock.tick(30)