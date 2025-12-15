import pygame, random
from circleshape import *
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__ (self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_one = Asteroid(self.position.x,self.position.y,self.new_radius)
        new_asteroid_one.velocity = self.velocity.rotate(angle) * 1.2
        new_asteroid_two = Asteroid(self.position.x,self.position.y,self.new_radius)
        new_asteroid_two.velocity = self.velocity.rotate(-angle) * 1.2

