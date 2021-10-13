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


def minimax(maximizing, board, depth):
      board_copy = deepcopy(board)

      if check_victory(PLAYER_1, board_copy):
            return 1, None
      elif check_victory(PLAYER_2, board_copy):
            return -1, None
      elif depth == 0:
            return 0, None

      found_empty = True
      for n in range(1,len(BOARD)+1):
            if is_occupied(n, BOARD):
                  found_empty = False  

      if not found_empty:
            return 0, None

      if maximizing:
            bestScore = -1000
            bestMove = 1
            for move in get_possible_moves(board_copy):
                  if make_move(move, PLAYER_1, board_copy):
                        score = minimax(False, board_copy, depth - 1)[0]
                  else:
                        return bestScore, bestMove
                  if (score > bestScore):
                        bestScore = score
                        bestMove = move
                        
                  for n in range(depth):
                        log.write("------")
                  log.write(str(depth)+" best move [MAX]: "+str(bestMove)+"\n")
            return bestScore, bestMove 

      else:
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
                        log.write("----")
                  log.write(str(depth)+" best move [MIN]: "+str(bestMove)+"\n")
            return bestScore, bestMove



def play_game():
      current_player = PLAYER_2
      board = deepcopy(BOARD)
      print_board(board)
      game_round = 0
      while True:
            log.write("\n\n\n==========round: "+str(game_round)+"==========\n")

            if current_player == PLAYER_1:
                  move = minimax(True, board, 20)[1]
                  if move != None:
                        if make_move(move, PLAYER_1, board):
                              print("\nbots turn, it made the move: "+str(move))
                              current_player = PLAYER_2
                              print_board(board)
                              game_round += 1
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

arg = sys.argv[1]

if arg == "game":
      play_game()
elif arg == "ai":
      ai_game()