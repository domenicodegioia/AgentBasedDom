from game.games import JumpingFrogsGame
from game.search import *

game = JumpingFrogsGame(N=2)
player1 = Random(game=game)
player2 = Minimax(game=game)

state = game.initial_state
moves = game.play(player_one=player1, player_two=player2)
