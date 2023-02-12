# Copyright (c) 2021 Johannes Thorén
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime

PLAYER_1 = "X"
PLAYER_2 = "O"
BLANK = " "

now = datetime.now()
game = open("game-"+now.strftime("%d-%m-%Y %H-%M-%S")+".txt","a+")

BOARD = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}



# Checks all possible victory states in tic tac toe and checks if specified player meets the 
# rules. checks if victory#
def check_victory(player, board):
    if board[1] == player and board[2] == player and board[3] == player:
        return True
    elif board[4] == player and board[5] == player and board[6] == player:
        return True
    elif board[7] == player and board[8] == player and board[9] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[3] == player and board[6] == player and board[9] == player:
        return True
    elif board[1] == player and board[5] == player and board[9] == player:
        return True
    elif board[7] == player and board[5] == player and board[3] == player:
        return True
    else:
        return False


def is_occupied(pos, board):
    return board[pos] != BLANK


def make_move(pos, player, board):

    # checks if a move a is leagal
    # and if so then make that move and return true 
    if is_occupied(pos, board):
        return False
    else:
        board[pos] = player
        return True

# prints the board to terminal and writes to log file
def print_board(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    game.write(board[1]+"|"+board[2]+"|"+board[3]+"\n")
    print("-+-+-")
    game.write("-+-+-\n")
    print(board[4]+"|"+board[5]+"|"+board[6])
    game.write(board[4]+"|"+board[5]+"|"+board[6]+"\n")
    print("-+-+- ")
    game.write("-+-+-\n")
    print(board[7]+"|"+board[8]+"|"+board[9])
    game.write(board[7]+"|"+board[8]+"|"+board[9]+"\n")
    game.write("\n")
