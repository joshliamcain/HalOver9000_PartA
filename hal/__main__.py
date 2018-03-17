
from hal.watch_your_back import GameState

BOARD_LINES = 8
MASSACRE = "Massacre"
MOVES = "Moves"


def get_input(get_line):
	game_board = []
	for _ in range(BOARD_LINES):
		game_board.append(str(get_line()).split(" "))
	game = GameState(game_board)
	mode = str(get_line())
	return mode, game


def run_mode(mode, game):
	if mode == MOVES:
		return moves(game)
	elif mode == MASSACRE:
		return massacre(game)
	else:
		raise ValueError("Incorrect game mode")


def massacre(game):
	return "Massacre"


def moves(game):
	return "Move"


if __name__ == "__main__":
	try:
		mode, game = get_input(input)
		output = run_mode(mode, game)
		print(output)
	except Exception as big_error:
		print("Something went wrong: " + str(big_error))
