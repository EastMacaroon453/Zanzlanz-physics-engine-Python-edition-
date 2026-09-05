# wall.py
import pygame
import math
from settings import *

class Wall:
    def __init__(self, ax, ay, bx, by, w):
        self.ax = ax # x-position of point a
        self.ay = ay # y-position of point a
        self.bx = bx # x-position of point b
        self.by = by # y-position of point b
        self.w = w # width

        # distance math
        dx = bx - ax # difference math
        dy = by - ay # and such
        length = math.sqrt(dx * dx + dy * dy) # "please continue, with te pytagorithian, theorem."
        self.l = length
        self.nx = -dy / length # "WHAAAT setting the normal x to -y?"
        self.ny = dx / length # yes im doing it to rotate it 90 degrees...

    def render(self, surface : pygame.Surface):
        pygame.draw.line(surface, "white", # the line
        ((self.ax + WIDTH/2), (HEIGHT/2 - self.ay)),
        ((self.bx + WIDTH/2), (HEIGHT/2 - self.by)),
        self.w)

        pygame.draw.circle(surface, "white", # round edge (:
        ((self.ax + WIDTH/2),
         (HEIGHT/2 - self.ay)),
         self.w/2)

        pygame.draw.circle(surface, "white", # round edge (;
        ((self.bx + WIDTH/2),
        (HEIGHT/2 - self.by)),
        self.w/2)

        #pygame.draw.line(surface, # debug red line
        #"red",
        #(self.ax + WIDTH/2, HEIGHT/2 - self.ay),
        #(self.ax + self.nx * 50 + WIDTH/2,
        #HEIGHT/2 - (self.ay + self.ny * 50)),
        #2)

# distance from any point! yay!
def distance(x1, y1, x2, y2):
    dist_x = x2 - x1
    dist_y = y2 - y1
    distance = math.sqrt(dist_x*dist_x + dist_y * dist_y)
    return(distance)