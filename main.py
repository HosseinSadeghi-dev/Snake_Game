import snake
import fruit
import pygame
import os


class Game:
    def __init__(self):
        os.system('cls||clear')
        self.width = 600
        self.height = 500
        pygame.init()
        # self.font = pygame.font.Font(pygame.font.match_font('Atlantic Cruise'), 14)
        self.font = pygame.font.Font('assets/fonts/Atlantic_Cruise.ttf', 14)

        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.difficulty = choose_difficulty(self.width, self.height, self.window)

        self.snake = snake.Snake(self.width, self.height, self.window, self.difficulty)
        self.fruit = fruit.Fruit(self.width, self.height, self.window, self.snake)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.x_change != 1:
                        self.snake.x_change = -1
                        self.snake.y_change = 0
                    elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.x_change != -1:
                        self.snake.x_change = 1
                        self.snake.y_change = 0
                    elif (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.y_change != -1:
                        self.snake.y_change = 1
                        self.snake.x_change = 0
                    elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.y_change != 1:
                        self.snake.y_change = -1
                        self.snake.x_change = 0
                    elif event.key == pygame.K_ESCAPE:
                        exit()

            self.window.fill((0, 0, 0))  # Background

            self.snake.move(self.fruit)

            # check snake is alive or not
            if not self.snake.alive:
                break

            self.snake.show()
            self.fruit.show()

            # Show Score
            score = self.font.render(f"Score: {self.snake.score}", True, (255, 237, 0))
            score_box = score.get_rect(center=(self.width / 2, self.height - 10))
            self.window.blit(score, score_box)

            pygame.display.update()  # Update Display
            self.clock.tick(60)  # FPS
        gameover(self.window, self.width, self.height, self.snake.score)


def choose_difficulty(width, height, window):
    pygame.init()
    font = pygame.font.Font('assets/fonts/Atlantic_Cruise.ttf', 40)

    easy = font.render('1- Easy', True, (255, 255, 255))
    easy_box = easy.get_rect(center=(width / 2, height / 2 - 60))

    medium = font.render('2- Medium', True, (255, 255, 255))
    medium_box = medium.get_rect(center=(width / 2, height / 2 - 20))

    hard = font.render('3- Hard', True, (255, 255, 255))
    hard_box = hard.get_rect(center=(width / 2, height / 2 + 20))

    extreme = font.render('4- I Dare You To Choose', True, (255, 255, 255))
    extreme_box = extreme.get_rect(center=(width / 2, height / 2 + 60))

    txt_1 = font.render(f"Esc To Exit", True, (255, 255, 255))
    text_1 = txt_1.get_rect(center=(width / 2, height / 2 + 120))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == 1073741913:
                    return 1
                elif event.key == pygame.K_2 or event.key == 1073741914:
                    return 3
                elif event.key == pygame.K_3 or event.key == 1073741915:
                    return 5
                elif event.key == pygame.K_4 or event.key == 1073741916:
                    return 8
                elif event.key == pygame.K_ESCAPE:
                    exit()

        window.blit(easy, easy_box)
        window.blit(medium, medium_box)
        window.blit(hard, hard_box)
        window.blit(extreme, extreme_box)
        window.blit(txt_1, text_1)
        pygame.display.update()


def instruction():
    return True


def main():
    game = Game()
    game.play()


def gameover(window, width, height, user_score):
    pygame.init()
    # font = pygame.font.Font(pygame.font.match_font('Atlantic Cruise'), 40)
    font = pygame.font.Font('assets/fonts/Atlantic_Cruise.ttf', 40)

    alert = font.render(f"GAMEOVER !!!", True, (255, 255, 255))
    alert_box = alert.get_rect(center=(width / 2, height / 2 - 70))

    print('user_score', user_score)
    score = font.render(f'SCORE : {user_score}', True, (255, 255, 255))
    score_box = score.get_rect(center=(width / 2, height / 2 - 30))

    txt = font.render(f"Press Enter To PLAY AGAIN", True, (255, 255, 255))
    text = txt.get_rect(center=(width / 2, height / 2 + 30))

    txt_1 = font.render(f"Press Esc To Exit", True, (255, 255, 255))
    text_1 = txt_1.get_rect(center=(width / 2, height / 2 + 70))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == 13:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    exit()

        window.blit(alert, alert_box)
        window.blit(score, score_box)
        window.blit(txt, text)
        window.blit(txt_1, text_1)
        pygame.display.update()


if __name__ == '__main__':
    main()
