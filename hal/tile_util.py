from collections import namedtuple
from numbers import Real
from math import hypot

_TileTuple = namedtuple('Tile','c, r')

class T(_TileTuple):

	def __str__(self):
		return "({},{})".format(self.c,self.r)

	def __repr__(self):
		return str(self)

	def between(self, lo, hi):
		above_lo = self.r>=lo.r and self.c>=lo.c
		below_hi = self.r<=hi.r and self.c<=hi.c
		return above_lo and below_hi

	def __add__(self, tile):
		assert isinstance(tile, T) and len(tile) == 2
		return T(self.c+tile.c, self.r+tile.r)

	def __rsub__(self, tile):
		return self - tile

	def __radd__(self, tile):
		return self + tile

	def __sub__(self, tile):
		return self + -1*tile

	def __mul__(self, scalar):
		assert isinstance(scalar, Real)
		return T(self.c*scalar, self.r*scalar)

	def __rmul__(self, scalar):
		return self * scalar

	def hypot(self):
		return int(hypot(self.c, self.r))

	def is_diag(self):
		return (self.c != 0) and (self.r != 0)
