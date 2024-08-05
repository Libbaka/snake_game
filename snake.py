import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Had (Snake)')

# Třída pro hada
class Snake:
    def __init__(self):
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -GRID_SIZE)
        self.grow = False

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + x) % WIDTH), (cur[1] + y) % HEIGHT)

        if new in self.positions:
            return False
        else:
            self.positions = [new] + self.positions
            if not self.grow:
                self.positions.pop()
            else:
                self.grow = False
            return True

    def reset(self):
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -GRID_SIZE)

    def change_direction(self, dir):
        if (dir[0] * -1, dir[1] * -1) != self.direction:
            self.direction = dir

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, GREEN, pygame.Rect(p[0], p[1], GRID_SIZE, GRID_SIZE))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    self.change_direction((0, GRID_SIZE))
                elif event.key == pygame.K_LEFT:
                    self.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    self.change_direction((GRID_SIZE, 0))

# Třída pro jídlo
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    game_over = False

    while True:
        if not game_over:
            snake.handle_keys()
            if not snake.update():
                game_over = True

            if snake.get_head_position() == food.position:
                snake.grow = True
                food.randomize_position()

            screen.fill(BLACK)
            snake.draw(screen)
            food.draw(screen)
            pygame.display.update()
            clock.tick(FPS)
        else:
            screen.fill(BLACK)
            font = pygame.font.SysFont(None, 55)
            text = font.render("Game Over", True, WHITE)
            screen.blit(text, [WIDTH // 4, HEIGHT // 2])
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
