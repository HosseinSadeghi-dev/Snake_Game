import snake
import fruit
import pygame
import os    
class Game:
    def __init__(self, difficulity):
        os.system('cls||clear')
        self.width = 600
        self.height = 500
        self.difficulity = difficulity
        pygame.init()
        # self.font = pygame.font.Font(pygame.font.match_font('Atlantic Cruise'), 14)
        self.font = pygame.font.Font('assets/fonts/Atlantic_Cruise.ttf', 14)

        self.window = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()

        self.snake = snake.Snake(self.width, self.height, self.window, self.difficulity)  
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
                    elif (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.y_change != 1:
                        self.snake.y_change = 1
                        self.snake.x_change = 0
                    elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.y_change != -1:
                        self.snake.y_change = -1
                        self.snake.x_change = 0

            self.window.fill((0, 0, 0)) #Background
            
            self.snake.move(self.fruit)

            #check snake is alive or not
            if self.snake.alive == False:
                break

            self.snake.show()
            self.fruit.show()

            #Show Score
            score = self.font.render(f"Score: {self.snake.score}", True, (255, 237, 0))
            score_box = score.get_rect(center = (self.width / 2, self.height - 10) )
            self.window.blit(score, score_box)

            pygame.display.update() #Update Display
            self.clock.tick(60) #FPS
        gameover(self.window, self.width, self.height, self.snake.score)

def choose_difficulity():
    return 3

def instruction():
    return True

def main():
    game = Game(choose_difficulity())
    game.play()

def gameover(window, width, height, user_score):
    pygame.init()
    # font = pygame.font.Font(pygame.font.match_font('Atlantic Cruise'), 40)
    font = pygame.font.Font('assets/fonts/Atlantic_Cruise.ttf', 40)
    alert = font.render(f"GAMEOVER !!!", True, (255, 255, 255))
    score = font.render(f"SCORE : {user_score}", True, (255, 255, 255))
    alert_box = alert.get_rect(center = (width / 2, height / 2) )
    score_box = score.get_rect(center = (width / 2, height / 2 + 40) )
    print("SCOOOOORe", user_score)

    while True:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or event.key == 13:
                        main()
                    elif event.key == pygame.K_ESCAPE:
                        exit()
        
        window.blit(alert, alert_box)
        window.blit(score, score_box)
        pygame.display.update()

if __name__ == '__main__':
    main()
    


