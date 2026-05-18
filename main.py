import pygame
import sys
 
# --- Configuration ---
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
 
BG_COLOR = (30, 30, 46)
 
# Liste de carrés : (x, y, largeur, hauteur, couleur)
squares = [
    (100, 100, 80, 80, (80, 160, 255)),
    (250, 200, 60, 60, (255, 160, 80)),
    (400, 150, 100, 100, (100, 220, 120)),
    (580, 300, 70, 70, (220, 100, 180)),
]
 
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
 
    for (x, y, w, h, color) in squares:
        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
 
    pygame.display.flip()
    clock.tick(FPS)
