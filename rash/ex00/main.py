#!/bin/env python3
from check_mate import checkmate
def main():
    board = """\
R...
.K..
..P.
....\
"""
    board = board.splitlines()
    for row in board:
        print(row)
    checkmate(board)

if __name__ == "__main__":
    main()