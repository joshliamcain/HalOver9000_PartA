from hal.graph_util import Graph
from hal.watch_your_back import WatchYourBack, Players
from copy import deepcopy
import pprint

def eval(game):
		return game.numpieces(Players.BLACK) - game.numpieces(Players.WHITE)

def goal_test(game):
	return game.numpieces(Players.BLACK) == 0

def movecopy(game, frm, to):
	g = deepcopy(game)
	g.move(frm, to)
	return g

def expandfunc(parent):
	possiblemoves = parent.obj.possible_moves(Players.WHITE)
	child_nodes = []
	for (frm, to) in possiblemoves:
		child_game = movecopy(parent.obj, frm, to)
		child_node = Graph.N(
			eval=eval(child_game),
			obj=child_game,
			parent=parent,
			operation=(frm, to),
			depth=parent.depth+1,
			isgoal=goal_test(child_game))
		child_nodes.append(child_node)
	return child_nodes

def kill_black_sequence(game):

	start_node = Graph.N(
		eval=eval(game),
		obj=game,
		parent=None,
		operation=None,
		depth=0,
		isgoal=goal_test(game))

	return Graph.search(start_node, expandfunc, 100)
