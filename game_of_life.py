import pygame
from pygame.locals import *
from random import randint


class GameOfLife:

    def __init__(self, width=800, height=600, cell_size=20, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        # count of cells horizontal and vertical
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = speed

    def draw_lines(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('green'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('green'),
                             (0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('GAME OF LIFE')
        self.screen.fill(pygame.Color('black'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self):
        grid = []
        for i in range(self.cell_height):
            line = [randint(0, 1) for i in range(self.cell_width)]
            grid.append(line)
        return grid

    def draw_grid(self):
        grid = self.create_grid()
        for y, x_list in enumerate(grid):
            for x, value in enumerate(x_list):
                if value == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))


if __name__ == '__main__':
    game = GameOfLife(1000, 800, 20, 1)
    game.run()
