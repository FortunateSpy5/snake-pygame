import pygame
import random
from time import sleep

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.size = 800
        self.divisions = 20
        self.length = 40
        self.screen = pygame.display.set_mode((self.size, self.size))
        self.font = pygame.font.Font('GamePlayed.ttf', 25)
        self.fps = 200
        self.interval = 50
        self.color = (255, 255, 0)
        self.food_color = (50, 200, 50)
        self.bg = (35, 35, 35)
        self.sound_eat = pygame.mixer.Sound('eat.wav')
        self.sound_dead = pygame.mixer.Sound('dead.wav')
        self.sound_eat.set_volume(0.5)
        self.sound_dead.set_volume(0.3)
        self.high_score = 0
        self.pause = True
        self.score = 0
        self.snake = [
            [self.divisions // 2 - 1, self.divisions // 2],
            [self.divisions // 2 - 1, self.divisions // 2 - 1],
            [self.divisions // 2 - 1, self.divisions // 2 - 2]
        ]
        self.head = self.snake[-1]
        self.direction = 0
        self.prev_direction = 0
        self.counter = 1
        self.food = self.get_food()

    def reset(self):
        self.high_score = max(self.score, self.high_score)
        self.snake = [
            [self.divisions // 2 - 1, self.divisions // 2],
            [self.divisions // 2 - 1, self.divisions // 2 - 1],
            [self.divisions // 2 - 1, self.divisions // 2 - 2]
        ]
        self.head = self.snake[-1]
        self.direction = 0
        self.prev_direction = 0
        self.counter = 1
        self.food = self.get_food()
        self.pause = True
        self.score = 0

    def get_food(self):
        x = random.randint(0, self.divisions - 1)
        y = random.randint(0, self.divisions - 1)
        while [x, y] in self.snake:
            x = random.randint(0, self.divisions)
            y = random.randint(0, self.divisions)
        return [x, y]

    def play(self):
        clock = pygame.time.Clock()
        self.draw()
        pygame.display.update()

        while True:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.direction = 0
            if keys[pygame.K_a]:
                self.direction = 3
            if keys[pygame.K_s]:
                self.direction = 2
            if keys[pygame.K_d]:
                self.direction = 1
            if keys[pygame.K_ESCAPE]:
                self.pause = not self.pause
                self.draw()
                pygame.display.update()
                sleep(0.2)

            if self.pause:
                continue

            if self.counter % self.interval == 0:
                if abs(self.direction - self.prev_direction) == 2:
                    self.direction = self.prev_direction
                else:
                    self.prev_direction = self.direction

                if self.direction == 0:
                    self.snake.append([self.snake[-1][0], (self.snake[-1][1] - 1 + self.divisions) % self.divisions])
                elif self.direction == 1:
                    self.snake.append([(self.snake[-1][0] + 1) % self.divisions, self.snake[-1][1]])
                elif self.direction == 2:
                    self.snake.append([self.snake[-1][0], (self.snake[-1][1] + 1) % self.divisions])
                elif self.direction == 3:
                    self.snake.append([(self.snake[-1][0] - 1 + self.divisions) % self.divisions, self.snake[-1][1]])

                if self.food not in self.snake:
                    self.snake.pop(0)
                else:
                    self.score += 1
                    self.sound_eat.play()
                    self.food = self.get_food()

                self.head = self.snake[-1]

                if self.snake.count(self.head) > 1:
                    self.sound_dead.play()
                    self.reset()

                self.draw()
                pygame.display.update()

            self.counter += 1

    def draw(self):
        pygame.draw.rect(self.screen, self.bg, pygame.Rect(0, 0, self.size, self.size))
        pygame.draw.rect(self.screen, self.food_color, pygame.Rect(self.food[0] * 40, self.food[1] * 40, 40, 40))
        for x, y in self.snake:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(x * 40, y * 40, 40, 40))
        self.screen.blit(self.font.render(f"High Score: {self.high_score}", True, (255, 255, 255)), (15, 10))
        self.screen.blit(self.font.render(f"Score: {self.score}", True, (255, 255, 255)), (15, 40))

        if self.pause:
            pygame.draw.rect(self.screen, self.bg, pygame.Rect(0, 0, self.size, self.size))
            text = self.font.render("Press ESC to continue", True, (255, 255, 255))
            self.screen.blit(text, ((self.size - text.get_rect().width) // 2, (self.size - text.get_rect().height) // 2))


if __name__ == '__main__':
    obj = SnakeGame()
    obj.play()
