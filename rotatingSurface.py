
import pygame

pygame.init()  
pygame.display.set_caption("fractal tree")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))  # creates game screen

color = (255, 255, 0)
size = 100

def squaretree(x,y,length,tilt,n):
    if n==0: return
    if n<6:
        color = (0, 255, 100)
    else:
        color = (100, 200, 100)
        
    #rotate square
    image = pygame.Surface((length, length)) 
    image.fill(color)
    image = pygame.transform.rotate(image, tilt)
    screen.blit(image, (x,y))

    #reset points for next round
    x1, y1 = x+length/2, y-length
    x2, y2 = x-length/2, y-length
    pygame.display.flip()
    
    #recursive call
    squaretree(x1,y1,length/2,tilt-45,n-1)
    squaretree(x2,y2,length/2,tilt+45,n-1)
    
squaretree(400,800,300,0,13)

