from cell import Cell
from posn import Posn
import pygame
from pygame.locals import *

class Universe:
    def __init__(self, x_size: int, y_size: int, cell_count: int):
        self.x_size = x_size
        self.y_size = y_size
        self.cell_count = cell_count
        Posn.MAX_X = x_size
        Posn.MAX_Y = y_size

    def init_cells(self):
        for i in range(self.cell_count):
            Cell()

    def run(self, seconds=10):
        pygame.init()

        print('Initted screen rect')
        screen = pygame.display.set_mode((self.x_size, self.y_size))
        pygame.display.set_caption('I hate pygame')

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        screen.blit(background, (0, 0))
        pygame.display.flip()

        print('Background size', background.get_size())

        clock = pygame.time.Clock()
        all_things = pygame.sprite.RenderUpdates()
        Cell.containers = all_things
        self.init_cells()

        while pygame.time.get_ticks() < seconds * 1000:
            all_things.clear(screen, background)
            all_things.update()
            dirty = all_things.draw(screen)
            pygame.display.update(dirty)

            print('Ticking')

            clock.tick(60)

        pygame.time.wait(1000)
        pygame.quit()
