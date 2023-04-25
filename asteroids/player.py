import math 
import pygame
from projectile import Projectile
from constants import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.points = [
            (self.x + 50 * math.sin(math.radians(self.angle)), self.y - 50 * math.cos(math.radians(self.angle))),
            (self.x - 20 * math.sin(math.radians(self.angle - 140)), self.y + 20 * math.cos(math.radians(self.angle - 140))),
            (self.x - 20 * math.sin(math.radians(self.angle - 180)), self.y + 20 * math.cos(math.radians(self.angle - 180))),
            (self.x - 20 * math.sin(math.radians(self.angle + 140)), self.y + 20 * math.cos(math.radians(self.angle + 140))),
        ]

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.angle -= PLAYER_ROTATE_SPEED
        if keys_pressed[pygame.K_RIGHT]:
            self.angle += PLAYER_ROTATE_SPEED

    def get_points(self):
        return [
            (self.x + 50 * math.sin(math.radians(self.angle)), self.y - 50 * math.cos(math.radians(self.angle))),
            (self.x - 20 * math.sin(math.radians(self.angle - 140)), self.y + 20 * math.cos(math.radians(self.angle - 140))),
            (self.x - 20 * math.sin(math.radians(self.angle - 180)), self.y + 20 * math.cos(math.radians(self.angle - 180))),
            (self.x - 20 * math.sin(math.radians(self.angle + 140)), self.y + 20 * math.cos(math.radians(self.angle + 140))),
        ]

    def draw(self, screen):
        points = self.get_points()
        pygame.draw.polygon(screen, WHITE, points)

    def get_center(self):
        points = self.get_points()
        center_x = sum(p[0] for p in points) / len(points)
        center_y = sum(p[1] for p in points) / len(points)
        return center_x, center_y
    
    def shoot(self, projectiles):
        x = self.x + 20 * math.sin(math.radians(self.angle))
        y = self.y - 20 * math.cos(math.radians(self.angle))
        projectile = Projectile(x, y, self.angle)
        projectiles.append(projectile)
        return -1
    
    def collides_with_asteroid(self, asteroid):
        center_x, center_y = self.get_center()
        distance = math.hypot(center_x - asteroid.x, center_y - asteroid.y)
        return distance < asteroid.radius