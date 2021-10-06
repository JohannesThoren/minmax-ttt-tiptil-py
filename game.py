PLAYER_1 = "X"
PLAYER_2 = "O"
BLANK = " "

BOARD = {
1: " ", 2: " ", 3: " ",
4: " ", 5: " ", 6: " ",
7: " ", 8: " ", 9: " "
}

def check_victory(player, board ):
      if board[1] == player and board[2] == player and board[3] == player:
            return True
      elif board[4] == player and board[5] == player and board[6] == player:
            return True
      elif board[7] == player and board[8] == player and board[9] == player:
            return True
      elif board[1] == player and board[5] == player and board[9] == player:
            return True      
      elif board[7] == player and board[5] == player and board[3] == player:
            return True
      else:
            return False

def is_occupied(pos, board):
      if board[pos] != BLANK:
            return True
      return False



def make_move(pos, player, board):
      if is_occupied(pos, board):
            return False
      else:
            board[pos] = player
            return True

def print_board(board):
      print(board[1]+"|"+board[2]+"|"+board[3])
      print("-+-+-")
      print(board[4]+"|"+board[5]+"|"+board[6])
      print("-+-+-")
      print(board[7]+"|"+board[8]+"|"+board[9])