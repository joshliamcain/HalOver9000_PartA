from collections import namedtuple
import time, math
from heapq import heappush, heappop

class Graph():
	
	_N = namedtuple("Node", 'eval, obj, parent, operation, depth, isgoal')

	class N(_N):

		def __str__(self):
			return "N"+str(obj)

		def __eq__(self, other):
			return self.eval == other.eval

		def __ne__(self, other):
			return self.eval != other.eval

		def __lt__(self, other):
			return self.eval < other.eval

		def __le__(self, other):
			return self.eval <= other.eval

		def __gt__(self, other):
			return self.eval > other.eval

		def __ge__(self, other):
			return self.eval >= other.eval


	#TODO: add optimality functionality
	#TODO: add option to use different queues functionality
	def search(start_node, expandfunc, time_limit):
		starttime = time.time()
		nodes = [start_node]
		i=0
		while (time.time() - starttime) < time_limit:
			node = heappop(nodes)
			#print("Popped:",node)
			if (time.time() - starttime)%2 <= 0.05:
				"""print(
					"t:", math.floor(time.time() - starttime),
					", i:", int(i),
					", e:", node.eval,
					", d", node.depth)"""
			if node.isgoal:
				return Graph.getpath(node)
			for child in expandfunc(node):
				heappush(nodes, child)
			i+=1
		raise Exception("Search timeout")


	def getpath(node):
		path = []
		while node.operation:
			path.append(node.operation)
			node = node.parent
		return path
