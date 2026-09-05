# main.py
import pygame
import sys
import math
from random import randint
from settings import *
from wall import Wall

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zanzlanz's physics engine ( Python edition )") # name
icon = pygame.image.load("zanzlanz_physics_python_icon.jpg") # icon
pygame.display.set_icon(icon) # display icon
clock = pygame.time.Clock()

FPS = 6
font = pygame.font.Font(None, 36)  # Default font, size 36


walls = [Wall(0, -300, 300, 0, 15), Wall(300, 0, 0, 300, 15), Wall(0, 300, -300, 0, 15), Wall(-300, 0, 0, -300, 15)]

#for _ in range(10):
#    rand_x = randint(-640, 640)
#    rand_y = randint(-360, 360)
#    balls.append(Ball(rand_x, rand_y, 10, 0, 10))

from objects import Ball, balls

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: # frame is complete ( i think )
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: # key presses/actions
            if event.key == pygame.K_r: # spawn medium ball
                random_xv = randint(-10, 10)
                random_yv = randint(-10, 10)
                balls.append(Ball(0, 0, random_xv, random_yv, 20))
            if event.key == pygame.K_t: # spawn smol ball
                random_xv = randint(-10, 10)
                random_yv = randint(-10, 10)
                balls.append(Ball(0, 0, random_xv, random_yv, 10))
            if event.key == pygame.K_e: # spawn BEEG ball
                random_xv = randint(-10, 10)
                random_yv = randint(-10, 10)
                balls.append(Ball(0, 0, random_xv, random_yv, 30))
            
            # "Oh you think you're very clever, don't you? Well how about we finish this with a little change of scenery?"
            if event.key == pygame.K_1: # scene 1; empty box
                walls = []
            if event.key == pygame.K_2: # scene 2; diamond ( 45deg square )
                walls = [Wall(0, -300, 300, 0, 15), Wall(300, 0, 0, 300, 15), Wall(0, 300, -300, 0, 15), Wall(-300, 0, 0, -300, 15)]
            if event.key == pygame.K_3:
                walls = [Wall(-300, -300, 300, -250, 15), Wall(300, -250, 300, -100, 15), Wall(300, -100, 0, 300, 15), Wall(0, 300, -300, 0, 15), Wall(-300, 0, -300, -300, 15)]

        # holding script
        if event.type == pygame.MOUSEBUTTONDOWN: # mouse press and hold
            for ball in balls:
                dx = MOUSE_X - ball.x
                dy = MOUSE_Y - ball.y
                dist = math.sqrt(dx*dx + dy*dy) # distance math
                if dist < ball.r:
                    ball.h = True
                    break
        if event.type == pygame.MOUSEBUTTONUP: # mouse release
            for ball in balls: # reset the ball that is being held
                if ball.h == True:
                    ball.h = False
                    break
    
    screen.fill((20, 20, 20)) # background

    for wall in walls: # render walls
        wall.render(screen)
    for ball in balls: # update and render balls/objects
        for _ in range(SUBSTEPS):
            ball.update(walls)
        ball.render(screen)

    FPS = clock.get_fps() # FPS,
    OBJECTS = len(balls) # and the amount of OBJECTS,
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos() # and mouse positions
    MOUSE_X -= WIDTH/2 # center MOUSE_X
    MOUSE_Y = HEIGHT/2 - MOUSE_Y # center MOUSE_Y

    fps_display = font.render(f"FPS: {FPS:.1f}", True, (255, 255, 255)) # make displays
    substeps_display = font.render(f"SUBSTEPS: {SUBSTEPS:.0f}", True, (255, 255, 255)) # here too..
    objects_display = font.render(f"OBJECTS: {OBJECTS:.0f}", True, (255, 255, 255)) # and here...
    mousepos_display = font.render(f"MOUSE POS: X/{MOUSE_X:.0f} Y/{MOUSE_Y:.0f}", True, (255, 255, 255)) # and the mouse pos!

    # and then finally display everything!
    screen.blit(fps_display, (10, 10))
    screen.blit(substeps_display, (10, 30))
    screen.blit(objects_display, (10, 50))
    screen.blit(mousepos_display, (10, 70))

    pygame.display.flip()
    clock.tick(60) 