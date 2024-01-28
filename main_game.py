from game.games import DummyGame
from game.search import *

dummy_game = DummyGame()
first_player = Random(game=dummy_game)
second_player = Minimax(game=dummy_game)

moves = dummy_game.play(first_player, second_player)


dummy_game = DummyGame()
search = AlphaBeta(game=dummy_game)

print(search.next_move(dummy_game.initial_state))
