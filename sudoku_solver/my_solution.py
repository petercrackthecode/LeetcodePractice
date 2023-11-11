# https://leetcode.com/problems/sudoku-solver/description/
from typing import List


def check_sub_sudoku(board, row, col, available_nums):
    # top, down, left, right
    [top, bottom, left, right] = [-1, -1, -1, -1]
    if col <= 2:
        left = 0
        right = 2
    elif 3 <= col and col <= 5:
        left = 3
        right = 5
    else:
        left = 6
        right = 8

    if row <= 2:
        top = 0
        bottom = 2
    elif 3 <= row and row <= 5:
        top = 3
        bottom = 5
    else:
        top = 6
        bottom = 8

    for i in range(top, bottom+1):
        for j in range(left, right+1):
            if board[i][j] != '.':
                curr_digit = int(board[i][j])
                available_nums.discard(curr_digit)


def get_avail_numbers(board, row, col):
    available_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # check_same_row
    for i in range(len(board[0])):
        if board[row][i] != '.':
            curr_digit = int(board[row][i])
            available_nums.discard(curr_digit)
    # check same column
    for j in range(len(board)):
        if board[j][col] != '.':
            curr_digit = int(board[j][col])
            available_nums.discard(curr_digit)
    # check sub sudoku
    check_sub_sudoku(board, row, col, available_nums)

    return available_nums


def fill_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                available_numbers = get_avail_numbers(board, i, j)
                for num in available_numbers:
                    board[i][j] = str(num)
                    if fill_board(board):  # Recurse with updated board state
                        return True
                    board[i][j] = '.'  # Backtrack
                return False  # No available number leads to a solution
    return True  # All cells filled


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        fill_board(board)
        return board
