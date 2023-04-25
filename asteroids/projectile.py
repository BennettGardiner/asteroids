import math 
import pygame

from constants import *

class Projectile:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.dx = PROJECTILE_SPEED * math.sin(math.radians(angle))
        self.dy = -PROJECTILE_SPEED * math.cos(math.radians(angle))

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < 0 or self.y < 0 or self.x > WIDTH or self.y > HEIGHT:
            return False
        return True

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 2)
