
from hal.watch_your_back import GameState

NUM_LINES = 8
MASSACRE = "Massacre"
MOVES = "Moves"


class GameState():
	def __init__(game_str):
		print(game_str)


def get_input():
	game_str = ""
	for _ in range(NUM_LINES):
		game_str += str(input())
	game = GameState(game_str)
	mode = str(input())
	return mode, game


def run_mode(mode, game):
	if mode == MOVES:
		return moves(game)
	elif mode == MASSACRE:
		return massacre(game)
	else:
		raise ValueError("Unknown game mode")


def massacre(game):
	return "Kill"


def moves(game):
	return "move"


if __name__ == "__main__":

	try:
		mode, game = get_input()
		ouptut = run_mode(mode, game)
		ptint(output)
	except Exception as error:
		print(error)
