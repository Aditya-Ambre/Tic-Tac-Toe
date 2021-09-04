import math
import random
from player import Humanplayer, RandomBot


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():

        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row)+' |')

    def make_move(self, square, letter):
        # if move valid , make the move
        # return true else return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    def winner(self, sqaure, letter):
        #check in rows
        row_ind = sqaure//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        #check in columns
        col_ind = sqaure % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        #check in diaggoals
        # check even positions
        if sqaure % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_square(self):
        return ' ' in self.board

    def nonempty_sqaure(self):
        return self.board.count(' ')


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_square():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter+' makes a move to square{}'.format(square))
                game.print_board()
                print('')  # line

            if game.current_winner:
                if print_game:
                    print(letter + " WINNER ")
                return letter
            # switch letters after ever move
            letter = 'O' if letter == 'X' else 'X'
            # change Os with Xs and vice versa
    if print_game:
        print("It\'s a tie")


if __name__ == "__main__":
    x_player = Humanplayer('X')
    o_player = RandomBot('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
