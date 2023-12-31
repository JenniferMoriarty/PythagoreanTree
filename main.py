import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window title
pygame.display.set_caption("Pythagorean Tree Fractal")

# Create the game screen
screen = pygame.display.set_mode((1500, 900))

def tree(ax, ay, bx, by, depth=0):


    if depth > 0:

        # (ax, ay) is bottom left corner
        # (bx, by) is bottom right corner

        # find the length of a side
        dx = bx - ax
        dy = #ADD CODE HERE

        # find top left corner
        x3 = bx - dy
        y3 = by - dx

        #find top right corner
        x4 = ax - dy
        y4 = ay - dx

        # find midpoint
        x5 = x4 + (dx - dy) / 2
        y5 = y4 - (dx + dy) / 2

       
        # Line from bottom left 
        pygame.draw.line(screen, (255,0,0), (ax , ay ), (bx , by )) #RED
        
        # line from bottom right corner to top right corner
        pygame.draw.line(screen, (0,255,0), (bx , by ), (x3 , y3 ))#GREEN
        
        # line from top left to top right
        pygame.draw.line(screen, (0,0,255), #ADD CODE HERE)#BLUE
        
        # line from top left to bottom left
        pygame.draw.line(screen, (255,255,255), #ADD CODE HERE)#WHITE

        pygame.display.flip()

        # Recursively call the tree function for the two smaller branches
        tree(x4, y4, x5, y5, depth - 1)  # Left branch
        tree(x5, y5, x3, y3, depth - 1)  # Right branch

# Initial call to the tree function to start the fractal
tree(100, 500, 200, 500, depth=8)

