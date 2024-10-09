############################################################
# Name: Flannery Sheets
# Name(s) of anyone worked with:
# Est time spent (hr): 1/2
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():

    def shape(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    
    gw = GWindow(WIDTH, HEIGHT)
    shape(100,100,100,100,'pink')
    shape(200,50,50,60,'light blue')
    shape(3,5,70,80,'yellow')
    shape(550,580,20,20,'green')
    shape(300,300,50,50,'purple')
    shape(250,250,200,200,'magenta')
    shape(500,250,30,100,'limegreen')
    shape(400,0,150,200,'#8e45ce')
    shape(0,400,200,200,'#93c47d')
    shape(0,250,100,40,'#e62d2d')
    shape(500,500,100,40,'#5b5fde')
    shape(250,500,220,80,'#f1c232')


if __name__ == '__main__':
    draw_image()
