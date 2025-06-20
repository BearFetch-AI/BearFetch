import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

CELL_SIZE = WIDTH // 3

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game board: 3x3 grid initialized to None
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Start with player X
current_player = "X"
game_over = False

# Draw grid lines
def draw_grid():
    for i in range(1, 3):
        # Vertical lines
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        # Horizontal lines
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

# Draw Xs and Os
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

# Check for a win
def check_winner(player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check for a tie
def check_tie():
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True

def ai_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        return (row, col)
    return None


# Game loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = mouse_y // CELL_SIZE
            clicked_col = mouse_x // CELL_SIZE

            # Place piece if cell is empty
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = "X"

                if check_winner("X"):
                    print("X wins!")
                    game_over = True

                elif check_tie():
                    print("It's a tie!")
                    game_over = True

                else:
                    # AI move (only if game isn't over)
                    ai_row, ai_col = ai_move()
    
                    if ai_row is not None:
                        if check_winner("O"):
                            print("O wins!")
                            game_over = True
                    elif check_tie():
                            print("It's a tie!")
                            game_over = True


    pygame.display.update()

pygame.quit()
sys.exit()
