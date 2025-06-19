import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Draw grid lines
def draw_grid():
    # Vertical lines
    pygame.draw.line(screen, BLACK, (100, 0), (100, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (200, 0), (200, HEIGHT), LINE_WIDTH)
    
    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, 100), (WIDTH, 100), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 200), (WIDTH, 200), LINE_WIDTH)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()
