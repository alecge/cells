import math
import random

class Posn:
    MAX_X = 640
    MAX_Y = 480

    def __init__(self, x: int, y: int, direction=0, velocity=0, max_x=MAX_X, max_y=MAX_Y):
        self.x = x
        self.y = y
        self.direction = direction
        self.velocity = velocity
        self.max_x = max_x
        self.max_y = max_y

        # Offset of current position from previous position
        self.diff_x = 0
        self.diff_y = 0

    def move(self, tick=1):
        self.diff_x = (math.cos(self.direction)) * self.velocity
        self.diff_y = math.sin(self.direction) * self.velocity
        self.x = int(self.x + self.diff_x)
        self.y = int(self.y + self.diff_y)

        if self.x > self.max_x:
            self.x = self.max_x

        if self.y > self.max_y:
            self.y = self.max_y

        if self.velocity < -10 or self.velocity > 10:
            self.velocity = random.randrange(-5, 5)

    @classmethod
    def generate(cls, max_x=MAX_X, max_y=MAX_Y):
        x = random.randrange(0, max_x)
        y = random.randrange(0, max_y)
        direction = random.uniform(0, 2 * math.pi)
        velocity = random.randrange(0, 5)

        return Posn(x, y, direction=direction, velocity=velocity, max_x=max_x, max_y=max_y)