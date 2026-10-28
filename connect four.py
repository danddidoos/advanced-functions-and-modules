import copy
import random

ROWS = 6
COLS = 7
EMPTY = "."
HUMAN = "X"
AI = "0"

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print()
    for row in board:
        print(" | " + " ".join(row) + " | ")
        print(" +" + "-" * (COLS * 2 + 1) + "+")
        print("    " + " ".join(str(i+1) for i in range(COLS)))
        print()

def get_valid_columns(board):
    return [col for col in range(COLS) if board[0][col] == EMPTY]

def drop_piece(board, col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return row
    return None
