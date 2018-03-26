from hal.watch_your_back import WatchYourBack, Players
from hal.tile_util import T


INPUT_LINES = 9
GAME_DIM = 8
WHITE_PIECE = "O"
BLACK_PIECE = "@"
MASSACRE = "Massacre"
MOVES = "Moves"


def parse_game_board(strings):
	rows = range(GAME_DIM)
	grid = [strings[r].split() for r in rows] #split strings into 2d grid
	white_pieces = get_pieces(grid, WHITE_PIECE)
	black_pieces = get_pieces(grid, BLACK_PIECE)
	game = WatchYourBack()
	game.dump_pieces(white_pieces, black_pieces)
	return game


def get_pieces(grid, target):
	"""returns a list of tiles which match the target"""
	rows = cols = range(GAME_DIM)
	def matching(col,row): return grid[row][col] == target
	return [T(c,r) for c in cols for r in rows if matching(c,r)]


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
	out = []
	print(game)
	out.append(str(len(game.possible_moves(Players.WHITE))))
	out.append(str(len(game.possible_moves(Players.BLACK))))
	return "\n".join(out)


def main(input_func, output_func):
	strings = [str(input_func()) for _ in range(INPUT_LINES)]
	mode = strings[GAME_DIM]
	game = parse_game_board(strings[:GAME_DIM])
	output = run_mode(mode, game)
	output_func(output)


if __name__ == "__main__":
	try:
		main(input, print)
	except Exception as err:
		print("Something went wrong: " + str(err))
