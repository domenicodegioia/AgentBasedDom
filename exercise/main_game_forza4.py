from game.games import Forza4
from game.search import *

game = Forza4()
player1 = Random(game=game)
player2 = Minimax(game=game)

state = game.initial_state
moves = game.play(player_one=player1, player_two=player2)