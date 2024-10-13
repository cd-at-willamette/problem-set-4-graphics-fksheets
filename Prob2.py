########################################
# Name: Flannery Sheets
# Collaborators:
# Estimated time spent (hrs): 1
########################################

from pgl import *

WIDTH = 600
HEIGHT = 600
BRICK_WIDTH = 70
BRICK_HEIGHT = 70
BRICKS_IN_BASE = 7

def draw_pyramid():

    gw = GWindow(WIDTH, HEIGHT)

    w = WIDTH
    h = HEIGHT
    x = BRICK_WIDTH
    y = BRICK_HEIGHT
    n = BRICKS_IN_BASE
    
    for i in range(n):
        row = n - i
        startx = (gw.get_width()- (row * x)) // 2
        starty = gw.get_height() - (row +1) * y

        for brick in range(row):
            width = startx + brick * x
            height = starty
            brick_rect = GRect(width,height,x,y)
            gw.add(brick_rect)




















if __name__ == '__main__':
    draw_pyramid()
