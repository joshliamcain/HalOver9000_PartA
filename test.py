
from hal.__main__ import run_mode
from hal.watch_your_back import GameState


print("\nTest 1 - Moves")

mode = "Moves"
game_str = ("X - - - O O - X\n"
			"- - - O - O O -\n"
			"O - O - - - - @\n"
			"- - - O O O - @\n"
			"- O O - - @ @ -\n"
			"- @ @ - @ @ @ -\n"
			"- @ @ @ - - - -\n"
			"X - - - - - - X\n")

game = GameState(game_str)
print(run_mode(mode, game))


print("\nTest 2 - Massacre")

mode = "Massacre"
game_str = ("X - - - O O - X\n"
			"- - - O - O O -\n"
			"O - O - - - - @\n"
			"- - - O O O - @\n"
			"- O O - - @ @ -\n"
			"- @ @ - @ @ @ -\n"
			"- @ @ @ - - - -\n"
			"X - - - - - - X\n")

game = GameState(game_str)
print(run_mode(mode, game))