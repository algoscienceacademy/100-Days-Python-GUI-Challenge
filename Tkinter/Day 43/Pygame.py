import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Constants
BOARD_SIZE = 8
SQUARE_SIZE = 80
WIDTH, HEIGHT = SQUARE_SIZE * BOARD_SIZE, SQUARE_SIZE * BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FPS = 60

# Load images
def load_images():
    pieces = ["wp", "bp", "wr", "br", "wn", "bn", "wb", "bb", "wq", "bq", "wk", "bk"]
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(
            pygame.image.load(os.path.join("images", f"{piece}.png")), (SQUARE_SIZE, SQUARE_SIZE)
        )
    return images

# Initial board setup
def create_board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]

# Draw the board
def draw_board(screen, board, images):
    screen.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = GRAY if (row + col) % 2 else WHITE
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece != "--":
                screen.blit(images[piece], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Handle piece selection and movement
def handle_click(board, pos, selected_piece, turn):
    row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
    piece = board[row][col]

    if selected_piece:
        # Move piece if square is empty or has opponent piece
        if board[row][col] == "--" or board[row][col][0] != selected_piece[1][0]:
            board[selected_piece[0][0]][selected_piece[0][1]] = "--"
            board[row][col] = selected_piece[1]
            return None, "b" if turn == "w" else "w"  # Toggle turn
        return selected_piece, turn  # Invalid move, keep selection
    elif piece != "--" and piece[0] == turn:
        return ((row, col), piece), turn  # Select piece

    return None, turn  # No selection

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Game")
    clock = pygame.time.Clock()
    images = load_images()
    board = create_board()
    selected_piece = None
    turn = "w"  # w for white's turn, b for black's turn

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected_piece, turn = handle_click(board, pos, selected_piece, turn)

        draw_board(screen, board, images)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
