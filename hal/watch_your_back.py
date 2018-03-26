from hal.tile_util import T
from enum import Enum
from copy import copy

class Players(Enum):
    BLACK = "black"
    WHITE = "white"

_CORNER = "corner"
_EMPTY = "empty"
_OUTSIDE = "out of bounds"

_NUM_PLAYERS = 2
_START_SIZE = 8

_DIRECTIONS = {T(1,0), T(0,1), T(-1,0), T(0,-1)}
_DIRECTION_PAIRS = {(T(1,0),T(-1,0)), (T(0,1), T(0,-1))}


class WatchYourBack():

    def __init__(self):
        self.__size = _START_SIZE
        self.__pieces = {Players.WHITE:set(), Players.BLACK:set()}


    def __str__(self):
        msg = list()
        msg.append("\n\tGame instance:")
        msg.append("\tWhite:" + str(self.__pieces[Players.WHITE]))
        msg.append("\tBlack:" + str(self.__pieces[Players.BLACK]))
        return "\n".join(msg)

    def __repr__(self):
        return str(self)

    def numpieces(self, player):
        return len(self.__pieces[player])


    def dump_pieces(self, white, black):
        """Places white and black lists of pieces. WARNING: This method 
        relies on correct lists of pieces being inserted
        """
        while white and black:
            self.place(white.pop(), Players.WHITE)
            self.place(black.pop(), Players.BLACK)


    def place(self, tile, player):
        """Places a peice
        Keyword arguments:
        tile -- location to place piece
        player -- colour of piece to place
        """
        if self.__valid_place(tile, player):
            self.__pieces[player].add(tile)
            self.__fight(player)
        else:
            raise Exception("Invalid place")


    def move(self, tile_from, tile_to):
        """Moves a peice
        Keyword arguments:
        tile_from -- location to move piece from
        tile_to -- location to move piece to
        """
        player = self.__get_tile(tile_from)
        if self.__valid_move(tile_from, tile_to):
            self.__pieces[player].remove(tile_from)
            self.__pieces[player].add(tile_to)
            self.__fight(player)
        else:
            raise Exception("Invalid move")


    def possible_moves(self, player):
        valid_moves = set()
        for piece in self.__pieces[player]:
            for vec in _DIRECTIONS:
                adj, further = (vec+piece), (piece + 2*vec)
                if self.__valid_move(piece, adj):
                    valid_moves.add((piece, adj))
                elif self.__valid_move(piece, further):
                    valid_moves.add((piece, further))
        return valid_moves


    def __fight(self, piece_owner):
        """Eliminates any peices as a result of a turn
        Keyword arguments:
        piece -- location of moved/placed piece
        player -- colour of piece
        """
        #Eliminate any tiles outside the board
        for player in Players:
            for piece in self.__pieces[player]:
                if self.__get_tile(piece) == _OUTSIDE:
                    self.__pieces[player].remove(piece)

        # kill surrounded opponent pieces first
        for player in Players:
            if player == piece_owner: continue
            for piece in copy(self.__pieces[player]):
                if self.__surrounded(piece, player):
                    self.__pieces[player].remove(piece)

        # kill surrounded player pieces
        for piece in copy(self.__pieces[piece_owner]):
                if self.__surrounded(piece, piece_owner):
                    self.__pieces[piece_owner].remove(piece)


    def __surrounded(self, piece, piece_owner):

        def is_deadly(tile, player):
            if tile in self.__get_corners(): return True
            is_a_player = self.__get_tile(tile) in Players
            is_current_player = self.__get_tile(tile) == player
            is_enemy_player = is_a_player and not is_current_player
            if is_enemy_player: return True
            return False

        for vec_pair in _DIRECTION_PAIRS:
            surrounded = True
            for vec in vec_pair:
                surrounded = surrounded and is_deadly(piece+vec, piece_owner)
            if surrounded: return True
        return False


    def __valid_place(self, tile, player):
        if self.__get_tile(tile) != _EMPTY: return False
        #TODO:check starting space
        return True


    def __valid_move(self, tile_from, tile_to):
        """Checks that a move is valid. Rules: must move a player piece, must
        move to empty tile, can't move diagonally, can't move nowhere or more
        than two tiles, if moving 2 tiles - there must be a piece inbetween
        """
        checks = []
        checks.append(self.__get_tile(tile_from) in Players)
        checks.append(self.__get_tile(tile_to) == _EMPTY)
        checks.append(not (tile_to - tile_from).is_diag())
        distance = (tile_to - tile_from).hypot()
        checks.append(distance > 0 and distance <= 2)
        if distance == 2:
            tile_between = 0.5*(tile_to - tile_from) + tile_from
            checks.append(self.__get_tile(tile_between) in Players)
        return False not in checks

    def __get_tile(self, tile):
        if tile in self.__pieces[Players.WHITE]:
            return Players.WHITE
        elif tile in self.__pieces[Players.BLACK]:
            return Players.BLACK
        elif tile in self.__get_corners():
            return _CORNER
        elif tile.between(T(0,0), T(self.__size-1, self.__size-1)):
            return _EMPTY
        else:
            return _OUTSIDE


    def __get_corners(self):
        fst, end = [0, self.__size-1]
        return {T(fst,fst),T(fst,end),T(end,end),T(end,fst)}
