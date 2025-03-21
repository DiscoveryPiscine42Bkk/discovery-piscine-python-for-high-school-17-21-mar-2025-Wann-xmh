#!/bin/env python3
from checkmate import checkmate

def main():
    board = """\
...Q
..K.
..P.
....\
"""
    board = board.splitlines()
    for row in board:
        print(row)
    checkmate(board)

if __name__ == "__main__":
     main()