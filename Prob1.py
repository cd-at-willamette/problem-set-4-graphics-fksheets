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

    def shape_r(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    
    def shape_o(x,y,w,h,color):
        oval = GOval(x,y,w,h)
        oval.set_filled(True)
        oval.set_color(color)
        gw.add(oval)
    
    def shape_ln(x,y,w,h,color):
        line = GLine(x,y,w,h)
        line.set_color(color)
        gw.add(line)
    


    
    gw = GWindow(WIDTH, HEIGHT)
    shape_r(100,100,100,100,'pink')
    shape_r(200,50,50,60,'light blue')
    shape_r(3,5,70,80,'yellow')
    shape_r(550,580,20,20,'green')
    shape_r(300,300,50,50,'purple')
    shape_r(250,250,200,200,'magenta')
    shape_r(500,250,30,100,'limegreen')
    shape_r(400,0,150,200,'#8e45ce')
    shape_r(0,400,200,200,'#93c47d')
    shape_r(0,250,100,40,'#e62d2d')
    shape_r(500,500,100,40,'#5b5fde')
    shape_r(250,500,220,80,'#f1c232')
    shape_o(100,200,300,100,'orange')
    shape_ln(0,120,400,3,'blue')
    shape_ln(600,120,400,20,'purple')
    gw.add(GLabel('coolio',500,580))
    


if __name__ == '__main__':
    draw_image()
