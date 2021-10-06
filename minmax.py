from game import check_victory, is_occupied, make_move, print_board, BOARD, PLAYER_1, PLAYER_2
import game
import math
from copy import deepcopy


def get_possible_moves(board):
      moves = []
      for n in range(1, len(board)+1):
            if is_occupied(n, board):
                  continue
            else:
                  moves.append(n)

      return moves


def minimax(maximizing, board):
      board_copy = deepcopy(board)
      print("\n")
      print_board(board_copy)

      if check_victory(PLAYER_1, board_copy):
            return 1, None
      elif check_victory(PLAYER_2, board_copy):
            return -1, None

      found_empty = True
      for n in range(1,len(BOARD)+1):
            if is_occupied(n, BOARD):
                  found_empty = False  

      if found_empty == False:
            return 0, None


      if maximizing:
            bestScore = -1000
            bestMove = 1
            for move in get_possible_moves(board_copy):
                  make_move(move, PLAYER_1, board_copy)
                  score = minimax(False, board_copy)[0]
                  if (score > bestScore):
                        bestScore = score
                        bestMove = move
                        print("max: "+str(bestMove))

            return bestScore, bestMove 

      else:
            bestScore = 1000
            bestMove = 1
            for move in get_possible_moves(board_copy):
                  make_move(move, PLAYER_2, board_copy)
                  score = minimax(True, board_copy)[0]
                  board_copy = board

                  if (score > bestScore):
                        bestScore = score
                        bestMove = move
                        print("min: "+str(bestMove))
            


            return bestScore, bestMove


current_player = PLAYER_2
board = deepcopy(BOARD)

while True:
      print("\n")
      print_board(board)



      if current_player == PLAYER_1:
            move = minimax(True, board)[1]
            make_move(move, PLAYER_1, board)
            current_player = PLAYER_2

      elif current_player == PLAYER_2:
            move = minimax(False, board)[1]
            make_move(move, PLAYER_2, board)
            current_player = PLAYER_1

      if check_victory(PLAYER_1, board):
            break
      elif check_victory(PLAYER_2, board):
            break