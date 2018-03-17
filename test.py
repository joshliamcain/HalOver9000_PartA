
from hal import __main__


def get_line_iter_func(fp):
	iterator = iter(fp.read().splitlines())
	def func():
		return next(iterator)
	return func


print("Test 1: Massacre")

fp = open("massacre_testinput.txt", "r")
next_line = get_line_iter_func(fp)

mode, game = __main__.get_input(next_line)
print(mode, game.board)
output = __main__.run_mode(mode, game)
print(output)

fp.close()



print("Test 2: Moves")

fp = open("moves_testinput.txt", "r")
next_line = get_line_iter_func(fp)

mode, game = __main__.get_input(next_line)
print(mode, game.board)
output = __main__.run_mode(mode, game)
print(output)

fp.close()