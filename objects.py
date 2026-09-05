# ball.py
import pygame
import math
from settings import *
from random import randint
#from level import *

#walls = [Wall(0, 0, 100, 0, 5)]
def wall_bounce(ball, wall, dist, nx, ny): # boing!
    if abs(dist)-ball.r-wall.w/2 < 0: # if touching the wall
            vn = ball.xv * nx + ball.yv * ny # speed across normal
            vt = ball.xv * ny + ball.yv * -nx # speed across tangent
            if vn <= 0: # if moving towards wall
                ball.xv = -(vn*nx) * (RESTITUTION) + (vt * ny) * (1 - FRICTION) # bounce of
                ball.yv = -(vn*ny) * (RESTITUTION) + (vt * -nx) * (1 - FRICTION) # bounce of
                ball.x += nx * -(dist - ball.r - wall.w/2) # gets the ball out of the wall
                ball.y += ny * -(dist - ball.r - wall.w/2) # gets the ball out of the wall

class Ball:
    def __init__(self, x, y, xv, yv, r):
        self.x = x # x position
        self.y = y # y position
        self.xv = xv # x velocity
        self.yv = yv # y velocity
        self.r = r # radius
        self.h = False # if you're holding the object
    
    def update(self, walls):
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        MOUSE_X -= WIDTH/2
        MOUSE_Y = HEIGHT/2 - MOUSE_Y
        if self.h == True:
            self.xv += (MOUSE_X - self.x)/5
            self.yv += (MOUSE_Y - self.y)/5
            self.x = MOUSE_X
            self.y = MOUSE_Y
        else:
            self.yv += GRAVITY

        # basic ground bounce lol
        if self.y - self.r < -(HEIGHT/2):
            self.yv *= -1 + FRICTION
            self.y = -(HEIGHT/2) + self.r
        if self.y + self.r > (HEIGHT/2):
            self.yv *= -1 + FRICTION
            self.y = (HEIGHT/2) - self.r
        if self.x - self.r < -(WIDTH/2):
            self.xv *= -1 + FRICTION
            self.x = -(WIDTH/2) + self.r
        if self.x + self.r > (WIDTH/2):
            self.xv *= -1 + FRICTION
            self.x = (WIDTH/2) - self.r

        for ball in balls:# ball-ball collisions
            if ball != self: # checks if the ball its checking is not itself
                dx = self.x - ball.x
                dy = self.y - ball.y # distance math
                dist = math.sqrt(dx*dx + dy*dy)
                if dist-ball.r-self.r < 0:
                    if dist == 0:
                        nx = 0
                        ny = 1
                    else:
                        nx = dx/dist # normal x
                        ny = dy/dist # normal y
                    vn = nx*(self.xv-ball.xv) + ny*(self.yv-ball.yv) # dot
                    vt = ny*(self.xv-ball.xv) + (-ny)*(self.yv-ball.yv) # dot
                    fx = vt/2*ny*FRICTION
                    fy = vt/2*-nx*FRICTION
                    fx += vn/2*nx*(1+RESTITUTION) # Powump! Custom bounce!
                    fy += vn/2*ny*(1+RESTITUTION)
                    self.xv -= fx # sets speed
                    self.yv -= fy
                    ball.xv += fx
                    ball.yv += fy
                    dist -= (self.r + ball.r) # make the distance account for the radiuses
                    self.x -= nx*(dist/2) # sets position
                    self.y -= ny*(dist/2)
                    ball.x += nx*(dist/2)
                    ball.y += ny*(dist/2)

        # wall bouce
        for wall in walls:
            distacrosswall = wall.ny*(self.x - wall.ax) + -wall.nx*(self.y - wall.ay)
            if distacrosswall > 0 and distacrosswall < wall.l: # if the ball is within the wall's edges
                dist = wall.nx*(self.x - wall.ax) + wall.ny*(self.y - wall.ay) # Dot products!
                wall_bounce(self, wall, dist, wall.nx, wall.ny)
            else: # when the ball isnt within the wall's edges
                if distacrosswall < 0: # if the ball is "behind" the wall
                    dx = self.x - wall.ax
                    dy = self.y - wall.ay
                    length = math.sqrt(dx * dx + dy * dy) # distance math
                    nx = dx / length # normal x calculation
                    ny = dy / length
                    dist = nx*(self.x - wall.ax) + ny*(self.y - wall.ay)
                    wall_bounce(self, wall, dist, nx, ny)
                else: # if the ball is on the other side
                    dx = self.x - wall.bx
                    dy = self.y - wall.by
                    length = math.sqrt(dx * dx + dy * dy) # distance math again
                    nx = dx / length # getting the normal x
                    ny = dy / length # and y
                    dist = nx*(self.x - wall.bx) + ny*(self.y - wall.by) # hey look! more dot products
                    wall_bounce(self, wall, dist, nx, ny)


        self.x += self.xv/(SUBSTEPS*2)
        self.y += self.yv/(SUBSTEPS*2)
    
    def render(self, surface : pygame.Surface):
        pygame.draw.circle(surface, "white", ((self.x + WIDTH/2), (HEIGHT/2 - self.y)), self.r) # white ball

        #pygame.draw.line(surface, # debug red line
        #"red",
        #(self.x + 640, 360 - self.y),
        #(self.x + self.xv * 2 + 640,
        #360 - (self.y + self.yv * 2)),
        #2)

# objects
random_xv = randint(-10, 10)
random_yv = randint(-10, 10)
balls = [Ball(0, 0, random_xv, random_yv, 20), Ball(0, 0, random_xv, random_yv, 20), Ball(0, 0, random_xv, random_yv, 20)]