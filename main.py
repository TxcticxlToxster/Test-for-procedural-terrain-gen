import pygame
import sys



class Block:
    def __init__(self,x,y,w,l,rgb):
        self.x = x
        self.y = y
        self.width = w
        self.length = l
        self.rgb = rgb
    
    def display(self):
        return (self.x,self.y,self.width,self.length,self.rgb)
        

def block_display(block):
    x0 = block.x + camera_x*-1
    y0 = block.y + camera_y*-1
    x1 = x0 - block.width
    y1 = y0 - block.length
    
    if (x0 >= 0 and x1 <= WINDOW_WIDTH) and (y0 >= 0 and y1 <= WINDOW_HEIGHT):
        pygame.draw.rect(screen, block.rgb, pygame.Rect(x0, y0, block.width, block.length))
        
# --- Configuration ---
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
BG_COLOR = (255,255,255)
camera_x = 100
camera_y = 0











display = [Block(0,0,10,10,(0,0,0))]
 
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fenêtre Pygame")
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    screen.fill(BG_COLOR)
 
    for el in display:
        block_display(el)
 
    pygame.display.flip()
    clock.tick(FPS)
