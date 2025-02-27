import pygame
from asteroid import Asteroid
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)
    
    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity * dt