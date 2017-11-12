from board import ChessBoard
from movement.base_logic import BaseLogic


class PawnMovementLogic(BaseLogic):
    def __init__(self, board=None, from_row=None, from_col=None,
                 to_row=None, to_col=None, player=None, is_opening_move=False):
        self.board = board
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col
        self.pawn = self.board[self.from_row][self.from_col]
        self.player = player
        self.is_opening_move = is_opening_move

    def move_pawn(self):
        if self.is_opening_move:
            self.board = self.opening_move()
        else:
            self.board = self.normal_move()
        self.board_format_print(self.board)
        return self.board

    def check_if_pawn(self):
        r = True
        if ChessBoard.PAWN not in self.pawn:
            self.print_padding("Piece is not a pawn")
            r = False
        return r

    def check_if_opening_move(self):
        r = False
        if self.is_opening_move:
            r = True
        return r

    def opening_move(self):
        if not self.check_if_pawn():
            return self.board

        if self.check_if_opening_move():
            if self.player == ChessBoard.PLAYER_ONE_INDICATOR:
                if self.from_row == self.to_row - 1:
                    if self.from_col == self.to_col:
                        self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                        self.board[self.to_row][self.to_col] = self.pawn
                elif self.from_row == self.to_row - 2:
                    if self.from_col == self.to_col:
                        self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                        self.board[self.to_row][self.to_col] = self.pawn
            elif self.player == ChessBoard.PLAYER_TWO_INDICATOR:
                if self.from_row == self.to_row + 1:
                    if self.from_col == self.to_col:
                        self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                        self.board[self.to_row][self.to_col] = self.pawn
                elif self.from_row == self.to_row + 2:
                    if self.from_col == self.to_col:
                        self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                        self.board[self.to_row][self.to_col] = self.pawn
        return self.board

    def normal_move(self):
        if self.player == ChessBoard.PLAYER_ONE_INDICATOR:
            if self.from_row == self.to_row - 1:
                if self.from_col == self.to_col:
                    self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                    self.board[self.to_row][self.to_col] = self.pawn
        elif self.player == ChessBoard.PLAYER_TWO_INDICATOR:
            if self.from_row == self.to_row + 1:
                if self.from_col == self.to_col:
                    self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                    self.board[self.to_row][self.to_col] = self.pawn
        return self.board

    def capture_piece(self):
        if self.player == ChessBoard.PLAYER_ONE_INDICATOR:
            if self.from_row == self.to_row - 1:
                if not self.board_sides_collision_detection():
                    return self.board
                if self.from_col == self.to_col - 1 or self.from_col == self.to_col + 1:
                    self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                    self.board[self.to_row][self.to_col] = self.pawn
        elif self.player == ChessBoard.PLAYER_TWO_INDICATOR:
            if self.from_row == self.to_row + 1:
                if not self.board_sides_collision_detection():
                    return self.board
                if self.from_col == self.to_col - 1 or self.from_col == self.to_col + 1:
                    self.board[self.from_row][self.from_col] = ChessBoard.EMPTY_TILE
                    self.board[self.to_row][self.to_col] = self.pawn
        self.board_format_print(self.board)
        return self.board

    def board_sides_collision_detection(self):
        r = True
        if self.to_col < 0 or self.to_col > 7:
            self.print_padding("Piece collided with side of board")
            r = False
        return r
