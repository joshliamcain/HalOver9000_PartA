
from main import main


def get_line_iter_func(fp):
	iterator = iter(fp.read().splitlines())
	def func():
		return next(iterator)
	return func

def get_print_func():
	def func(string):
		print(string)
	return func

if __name__ == "__main__":
	print("Test 1: Massacre")

	fp = open("massacre_testinput.txt", "r")
	main(get_line_iter_func(fp), get_print_func())
	fp.close()


	print("Test 2: Moves")

	fp = open("moves_testinput.txt", "r")
	main(get_line_iter_func(fp), get_print_func())
	fp.close()
