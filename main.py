#importing libraries
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Define constants for the frame
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Define colours
BLACK = (0, 0, 0)  #background where pacman can move
WHITE = (255, 255, 255)  #background
YELLOW = (255, 255, 0)  #pacman
GREEN = (0, 255, 0)  #food which is the point of the game
BLUE = (0, 0, 255)  #walls

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Define the game board
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
pacman_pos = (ROWS // 2, COLS // 2)
board[pacman_pos[0]][pacman_pos[1]] = 2  # Pacman

# Place walls and food randomly
for i in range(ROWS):
    for j in range(COLS):
        if i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1 or random.random(
        ) < 0.1:
            board[i][j] = 1  # Wall
        elif random.random() < 0.1:
            board[i][j] = 3  # Food

# Define movements
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#Using Backtracking to solve the maze
def draw_board():
    for i in range(ROWS):
        for j in range(COLS):
            color = BLACK
            if board[i][j] == 1:
                color = BLUE
            elif board[i][j] == 2:
                color = YELLOW
            elif board[i][j] == 3:
                color = GREEN
            pygame.draw.rect(
                screen, color,
                (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def move_pacman(new_pos):
    global pacman_pos
    x, y = pacman_pos
    nx, ny = new_pos
    if board[nx][ny] != 1:  # Not a wall
        if board[nx][ny] == 3:  # Food
            board[nx][ny] = 0
        board[x][y] = 0
        pacman_pos = new_pos
        board[nx][ny] = 2


# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: # W key to move up
                move_pacman((pacman_pos[0] - 1, pacman_pos[1]))
            elif event.key == pygame.K_s: # S key to move down
                move_pacman((pacman_pos[0] + 1, pacman_pos[1]))
            elif event.key == pygame.K_a: # A key to move left
                move_pacman((pacman_pos[0], pacman_pos[1] - 1))
            elif event.key == pygame.K_d: # D key to move right
                move_pacman((pacman_pos[0], pacman_pos[1] + 1))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
