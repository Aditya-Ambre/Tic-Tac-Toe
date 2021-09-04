import math
import random


class PLayer:
    def __init__(self, letter):
        # letter is  x or o
        self.letter = letter

    # next  move for the player


class RandomBot(PLayer):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class Humanplayer(PLayer):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        vaild_square = False
        val = None
        while not vaild_square:
            square = input(self.letter + '\'s turn input move (0-9): ')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                vaild_square = True
            except ValueError:
                print(" Invalid sqaure !!! ")
        return val


class GeniusComputer(PLayer):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get the square based off the algorithm
            sqaure = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == 'X 'else "X"

        if state.current_winner == other_player:
            return{'postion': None,
                   'score': 1*(state.num_empty_square()+1) if other_player == max_player else -1*(state.num_empty_squares()+1)}

        elif not state.empty_square():
            return {'positon': None, 'score': 0}

        if player == max_player:
            best = {'postion': None, 'score': -math.inf}

        else:
            best = {'postion': None, 'score': math.inf}
