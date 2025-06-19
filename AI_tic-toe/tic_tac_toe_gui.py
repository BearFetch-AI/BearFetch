import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

CELL_SIZE = WIDTH // 3

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game board: empty cells represented by None
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Player turn: "X" starts first
current_player = "X"

# Draw the board grid
def draw_grid():
    for i in range(1, 3):
        # Vertical lines
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        # Horizontal lines
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

# Draw X and O
def draw_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                # Draw X
                start_pos = (col * CELL_SIZE + 20, row * CELL_SIZE + 20)
                end_pos = (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + CELL_SIZE - 20)
                pygame.draw.line(screen, RED, start_pos, end_pos, LINE_WIDTH)
                pygame.draw.line(screen, RED, (start_pos[0], end_pos[1]), (end_pos[0], start_pos[1]), LINE_WIDTH)
            elif board[row][col] == "O":
                # Draw O
                center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
                radius = CELL_SIZE // 2 - 20
                pygame.draw.circle(screen, BLUE, center, radius, LINE_WIDTH)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = mouse_y // CELL_SIZE
            clicked_col = mouse_x // CELL_SIZE

            # Only place if cell is empty
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = current_player
                current_player = "O" if current_player == "X" else "X"

    pygame.display.update()

pygame.quit()
sys.exit()
