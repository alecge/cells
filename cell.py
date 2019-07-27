from posn import Posn
from random import Random
import math
import pygame


class Cell(pygame.sprite.Sprite):
    CELL_RADIUS = 4

    def __init__(self, coord=None, direction=0, velocity=0, cell_radius=CELL_RADIUS):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.coord = coord if coord else Posn.generate()
        self.rand = Random()

        self.image = pygame.Surface((cell_radius * 2, cell_radius * 2))
        self.image.fill(pygame.Color('green'))

        self.rect = self.image.get_rect()
        self.rect.x = self.coord.x
        self.rect.y = self.coord.y

    def update(self):
        self.move()

    def move(self):
        if self.rand.randrange(0, 100) < 40:
            self.coord.direction = self.rand.uniform(self.coord.direction - 0.5 * math.pi,
                                                     self.coord.direction + 0.5 * math.pi)

        if self.rand.randrange(0, 100) < 20:
            self.coord.velocity = self.rand.randrange(self.coord.velocity - 2, self.coord.velocity + 2)

        self.coord.move()
        self.rect.move_ip(self.coord.diff_x, self.coord.diff_y)
