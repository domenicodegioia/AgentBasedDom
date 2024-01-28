from game.games import TicTacToe
from game.search import *

game = TicTacToe()
player1 = Random(game=game)
player2 = Minimax(game=game)

state = game.initial_state
moves = game.play(player_one=player1, player_two=player2)