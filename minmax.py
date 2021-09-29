from game import BOARD_HEIGHT, BOARD_WIDTH
import game



game = game.Game()

def get_moves(board, current_player):
      moves = []

      for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                  if board[i][j].isOccupied:
                        continue
                  else:
                        moves.append((i,j))
      
      return moves


def minimax(maximizing):
      score = 0
      if maximizing


print(get_moves(game.board, game.currentPlayer))