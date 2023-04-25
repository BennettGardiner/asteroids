
import pygame
import math
import random

from constants import *

class Asteroid:
    def __init__(self, x, y, dx, dy, radius, level):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.level = level

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Wrap the asteroid's position
        self.x = self.x % WIDTH
        self.y = self.y % HEIGHT

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, width=2)

    def collides_with_projectile(self, projectile):
        distance = math.hypot(self.x - projectile.x, self.y - projectile.y)
        return distance < self.radius
    

def create_random_asteroid():
    edge = random.choice(['left', 'right', 'top', 'bottom'])
    if edge == 'left':
        x = 0
        y = random.randint(0, HEIGHT)
    elif edge == 'right':
        x = WIDTH
        y = random.randint(0, HEIGHT)
    elif edge == 'top':
        x = random.randint(0, WIDTH)
        y = 0
    else:  # 'bottom'
        x = random.randint(0, WIDTH)
        y = HEIGHT

    angle = random.uniform(0, 2 * math.pi)
    dx = ASTEROID_SPEED * math.cos(angle)
    dy = ASTEROID_SPEED * math.sin(angle)

    return Asteroid(x, y, dx, dy, ASTEROID_SIZE, level=3)

def create_smaller_asteroids(asteroid):
    smaller_asteroids = []
    for _ in range(2):
        angle = random.uniform(0, 2 * math.pi)
        dx = ASTEROID_SPEED * math.cos(angle)
        dy = ASTEROID_SPEED * math.sin(angle)
        smaller_asteroids.append(
            Asteroid(
                asteroid.x,
                asteroid.y,
                dx,
                dy,
                ASTEROID_SIZE * (asteroid.level - 1) / 3,
                asteroid.level - 1,
            )
        )
    return smaller_asteroids
