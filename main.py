import pygame
import math

pygame.init()
screen = pygame.display.set_mode((750, 650))
display = pygame.display.get_surface()


# ang = Angle, lng = length
def draw_tree(start, stop, ang, lng):
    if lng > 0:
        next_start = start + int(math.cos(math.radians(ang)) * lng * 10.0)
        next_stop = stop + int(math.sin(math.radians(ang)) * lng * 10.0)
        pygame.draw.line(display, (127, 255, 0), (start, stop), (next_start, next_stop), 1)
        draw_tree(next_start, next_stop, ang - 25, lng - 1)
        draw_tree(next_start, next_stop, ang + 25, lng - 1)


draw_tree(370, 650, -90, 10)
pygame.display.flip()
while True:
    pass
