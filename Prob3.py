########################################
# Name: Flannery Sheets
# Collaborators:
# Estimate time spent (hrs): 2
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    def center_square(square):
        square.set_location((GW_WIDTH - SQUARE_SIZE) / 2, (GW_HEIGHT - SQUARE_SIZE) / 2)

    # Create a square in the center of the window
    square = GRect(SQUARE_SIZE, SQUARE_SIZE)
    square.set_filled(True)
    square.set_color("hot pink")
    center_square(square)
    gw.add(square)

    # Initialize score label
    score_label = GLabel("Score: 0", SCORE_DX, GW_HEIGHT - SCORE_DY)
    gw.add(score_label)

    # Global score variable
    score = 0

    # Function to check if the mouse is inside the square
    def is_mouse_in_square(mx, my):
        sq_x = square.get_x()
        sq_y = square.get_y()
        return sq_x <= mx <= sq_x + SQUARE_SIZE and sq_y <= my <= sq_y + SQUARE_SIZE

    # Function to move the square to a new random position within window bounds
    def move_square_to_random_position():
        new_x = random.randint(0, GW_WIDTH - SQUARE_SIZE)
        new_y = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
        square.set_location(new_x, new_y)

    # Function to update score
    def update_score(new_score):
        global score
        score = new_score
        score_label.set_label(f"Score: {score}")

    # Event handler for mouse click
    def on_mouse_down(event):
        global score
        mx, my = event.get_x(), event.get_y()
        
        if is_mouse_in_square(mx, my):
            # If clicked inside the square, move it and update score
            move_square_to_random_position()
            update_score(score + 1)
        else:
            # Reset score if clicked outside the square
            update_score(0)

    # Add the mouse listener to the window
    gw.add_event_listener("mousedown", on_mouse_down)



if __name__ == '__main__':
    clicky_box()
