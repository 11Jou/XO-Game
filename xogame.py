import time
class XO:
    counter = 0
    def __init__(self , board):
        self.board = board

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end='  |  ')
            print('\n----------------')
    def positionIsAvailable(self,i,j):
        if self.board[int(i)][int(j)] == 'x' or self.board[int(i)][int(j)] == 'o':
            return False
        else:
            return True
    def set_char(self,position , char):
        position = position.split(' ')
        row = int(position[0]) - 1
        col = int(position[1]) - 1
        if self.positionIsAvailable(row, col):
            self.counter += 1
            self.board[row][col] = char
        else:
            print("This position is unavailable")
    def gameAvailable(self, player):
        # check for rows and col
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]) or (self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]):
                print("Congrats player {} won".format(player))
                return True
        # check for slope
        if (self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]) or (self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]):
            print("Congrats player {} won".format(player))
            return True
        # check game over
        if self.counter == 9:
            print("Game Over")
            return True
        return False
def startgame():
    print("Hello User \nWelcome to x.o game")
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game = XO(board)
    time.sleep(1)
    print("Start the game \n----------------------")
    time.sleep(1)
    player1 = input("Choose Your Letter x or o : ")
    last_char = player1
    current = player1
    index = {'1': '1 1', '2': '1 2', '3': '1 3', '4': '2 1', '5': '2 2',
             '6': '2 3', '7': '3 1', '8': '3 2', '9': '3 3'}
    game.print_board()
    while not game.gameAvailable(last_char):
        last_char = current
        position = input("Enter the position from 1 to 9 : ")
        game.set_char(index[position], last_char)
        game.print_board()
        if last_char == 'x':
            current = 'o'
        else:
            current = 'x'
startgame()
