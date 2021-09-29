BOARD_WIDTH = 8
BOARD_HEIGHT = 8



class Game():
      def __init__(self):
            self.__board = []
            self.__currentPlayer = 1

            self.__gen_board(BOARD_WIDTH, BOARD_HEIGHT)

      @property
      def currentPlayer(self):
            return self.__currentPlayer
      
      @property
      def board(self):
            return self.__board
      
      def next_player(self):
            if self.__currentPlayer == 1:
                  self.__currentPlayer = 2
            elif self.__currentPlayer  == 2:
                  self.__currentPlayer = 1

      def get_tile(self, pos):
            for i in range(BOARD_HEIGHT):
                  for j in range(BOARD_WIDTH):
                        if (i, j) == pos:
                              return self.board[i][j]

      def make_move(self, pos):
            tile = self.get_tile(pos)
            if tile.isOccupied:
                  return False
            else:
                  tile.makeMove()
            return


      def __gen_board(self, width, height):
            for i in range(BOARD_HEIGHT):
                  row = []
                  for j in range(BOARD_WIDTH):
                        tile = Tile()
                        tile.set_pos((i, j))
                        row.append(tile)

                  self.board.append(row)

      def print_board(self):
            for i in range(BOARD_HEIGHT):
                  row = ""
                  for j in range(BOARD_WIDTH):
                        row = row+str(self.board[i][j].getPlayer)+" "
                  print(row)

      def check_if_victory(self, player):
            for i in range(BOARD_HEIGHT):
                  for j in range(BOARD_WIDTH):
                        if i != 0 or i != BOARD_HEIGHT and j != 0 or j != BOARD_WIDTH:

                                    # , p , 
                                    # , p ,
                                    # , p ,
                                    if self.board[i+1][j].getPlayer == player and self.board[i-1][j].getPlayer == player:
                                          return True

                                    # , , p
                                    # , p ,
                                    # p , ,
                                    elif self.board[i+1][j-1].getPlayer == player and self.board[i-1][j+1].getPlayer == player:
                                          return True

                                    # p , ,
                                    # , p ,
                                    # , , p
                                    elif self.board[i-1][j-1].getPlayer == player and self.board[i+1][j+1].getPlayer == player:
                                          return True

                                    # , , ,
                                    # p p p
                                    # , , ,
                                    elif self.board[i][j-1].getPlayer == player and self.board[i][j+1].getPlayer == player:
                                          return True

                                    else:
                                          return False

            
class Tile():
      def __init__(self):
            self.__value = 0
            self.__pos = (0,0)

      def set_pos(self, pos):
            self.__pos = pos

      @property
      def getPlayer(self):
            return self.__value

      @property
      def isOccupied(self):
            if self.__value > 0:
                  return True
            else:
                  return False

      def make_move(self, player):
            if self.isOccupied:
                  return False
            else:
                  self.__value = player
                  return True



def start():
      game = Game()
      game.print_board()