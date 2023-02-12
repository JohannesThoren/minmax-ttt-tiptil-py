# Copyright (c) 2021 Johannes Thorén
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from game import check_victory, is_occupied, make_move, print_board, BOARD, PLAYER_1, PLAYER_2
import game
import math
from copy import deepcopy
from datetime import datetime

now = datetime.now()
log = open("tree-"+now.strftime("%d-%m-%Y %H-%M-%S")+".txt","a+")


def get_possible_moves(board):
      moves = []
      for n in range(1, len(board)+1):
            if is_occupied(n, board):
                  continue
            else:
                  moves.append(n)
      # print(moves)
      return moves


# minimax function, this is a recursive function
# it is the function that is the "ai"
# it returns the best move and a value of the move.
def minimax(maximizing, board, depth):
      board_copy = deepcopy(board)

      # Checks if either Player one or Player two won.
      # returns a value and none if someone won else
      # the move on to the next part of the code#
      if check_victory(PLAYER_1, board_copy):
            return 1, None
      elif check_victory(PLAYER_2, board_copy):
            return -1, None
      elif depth == 0:
            return 0, None

      # checks if the board is filled by checking all "cells" and if they are occupied.
      # found empty is by default False to then if there is an empty "cell" get set to True.
      # 
      # If the found_empty never gets set to True then the minimax function will return 0 as value and a "none" move #
      found_empty = False
      for n in range(1,len(BOARD)+1):
            if not is_occupied(n, BOARD):
                  found_empty = True

      if not found_empty:
            return 0, None

      # The maximizing boolean is checked and according to if it is true or false the reccursion call
      # to the minimax function has either true or false an argument.#
      if maximizing:
            # The default score and is a high negative number to make checking and comparing will be easier.
            # basically the default needs to be a low number so the scoring later in the code works. #
            bestScore = -1000

            # the best move can by default be set to anything. I choose 1 aka the first cell 
            bestMove = 1

            # this loop walks through all possible moves, and evaluates them by sending a temporary board 
            # with that move made through the minimax function. this will be done for each possible move # 
            for move in get_possible_moves(board_copy):

                  # if it is possible to make a specific move then set the score to the result of the recursive call to minimax. 
                  # else just return the bestScore and bestMove#
                  if make_move(move, PLAYER_1, board_copy):

                        score = minimax(False, board_copy, depth - 1)[0]
                  else:
                        return bestScore, bestMove

                  # this evaluates if the score received by the minimax function is more than best score
                  if (score > bestScore):
                        bestScore = score
                        bestMove = move
                        
                  # this loop is only used to format the output log files
                  for n in range(depth):
                        log.write("\t")
                  log.write(str(depth)+" best move [MAX]: "+str(bestMove)+"\n")

            return bestScore, bestMove 
      else:
            ##############################################
            # THIS WORKS THE SAME WAY ASE THE CODE ABOVE #
            # THE ONLY DIFFERENCE IS THE MINIMAX CALL    #
            # INSTEAD OF A FALSE  ARGUMENT IT HAS TRUE.  #
            # AND INSTEAD OF CHECKING IF SCORE IS LARGER #
            # IT CHECKS IF SCORE IS SMALLER              #
            ##############################################
            bestScore = 1000
            bestMove = 1
            for move in get_possible_moves(board_copy):
                  if make_move(move, PLAYER_2, board_copy):
                        score = minimax(True, board_copy, depth - 1)[0]
                  else:
                        return bestScore, bestMove


                  if (score < bestScore):
                        bestScore = score
                        bestMove = move  

                  for n in range(depth):
                        log.write("\t")
                  log.write(str(depth)+" best move [MIN]: "+str(bestMove)+"\n")
            return bestScore, bestMove



# This code is only used to actually play the game.
# it has a state machine that checks the current_player
# and does stuff accordingly. #
def play_game(start_player):
      current_player = start_player
      board = deepcopy(BOARD)
      print_board(board)
      game_round = 0
      while True:
            log.write("\n\n\n==========round: "+str(game_round)+"==========\n")

            if current_player == PLAYER_1:
                  move = minimax(True, board, 10)[1]
                  if move != None:
                        if make_move(move, PLAYER_1, board):
                              print("\nbots turn, it made the move: "+str(move))
                              current_player = PLAYER_2
                              print_board(board)
                              game_round += 1
                              log.write(f"The best move to make for player {PLAYER_1} is {move}")

                        else:
                              print("could not make move")



            elif current_player == PLAYER_2:
                  inp = int(input("your turn, make a move: "))
                  if make_move(inp, PLAYER_2, board):
                        current_player = PLAYER_1
                        print_board(board)
                        game_round += 1
                        log.write("player 2 made the move: "+str(inp)+"\n")


            if check_victory(PLAYER_1, board):
                  print("\nThe Bot Won!")
                  log.close()
                  break

            elif check_victory(PLAYER_2, board):
                  print("\nYou Won!")
                  break



def ai_game():
      game_round = 0
      row_1 = input("row1 to solve: ").upper().split(",")
      row_2 = input("row2 to solve: ").upper().split(",")
      row_3 = input("row3 to solve: ").upper().split(",")

      board = {
            1:row_1[0], 2:row_1[1], 3:row_1[2],
            4:row_2[0], 5:row_2[1], 6:row_2[2],
            7:row_3[0], 8:row_3[1], 9:row_3[2],

      }

      print(board)

      current_player = PLAYER_2

      depth = int(input("depth: "))

      while True:

            log.write("\n\n\n==========round: "+str(game_round)+"==========\n")
            
            if current_player == PLAYER_1:
                  move = minimax(True, board, depth)[1]
                  if move != None:
                        if make_move(move, PLAYER_1, board):
                              print("\nbot 1's turn, it made the move: "+str(move))
                              current_player = PLAYER_2
                              print_board(board)
                              game_round += 1
                              log.write(f"The best move to make for player {PLAYER_1} is {move}")
                        else:
                              print("could not make move")

            if current_player == PLAYER_2:
                  move = minimax(True, board, depth)[1]
                  if move != None:
                        if make_move(move, PLAYER_2, board):
                              print("\nbot 2's turn, it made the move: "+str(move))
                              current_player = PLAYER_1
                              print_board(board)
                              game_round += 1
                              log.write(f"The best move to make for player {PLAYER_2} is {move}")

                        else:
                              print("could not make move")

            

            if check_victory(PLAYER_1, board):
                  print("\nBot 1 Won!")
                  log.close()
                  break

            elif check_victory(PLAYER_2, board):
                  print("\nBot 2 Won!")
                  break




import sys
args = sys.argv


if len(args) < 2:
      print("needed arguments, minmax.py <mode ai/game> <starter me/bot>")
else:
      # this handles the commandline arguments to either play the game or let 2 ai's play against eachother
      if args[1] == "game":
            if len(args) >= 2:
                  if args[2] == "bot":
                        play_game(PLAYER_1)
                  if args[2] == "me":
                        play_game(PLAYER_2)
            else:
                  play_game(PLAYER_2)

      elif args[1] == "ai":
            ai_game()

      else:
            print("no mode selected, select either \"ai\" or \"game\"")