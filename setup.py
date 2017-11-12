from board import ChessBoard
from movement.pawn_movement_logic import PawnMovementLogic


def game_setup():
    chess_board = ChessBoard()
    chess_board.create_board()
    # print(chess_board.get_board())
    move = PawnMovementLogic(chess_board.get_board(), 1, 2, 3, 2, 0, True)
    move.move_pawn()
    move = PawnMovementLogic(chess_board.get_board(), 6, 6, 4, 6, 1, True)
    move.move_pawn()
    move = PawnMovementLogic(chess_board.get_board(), 3, 2, 4, 2, 0, False)
    move.move_pawn()


game_setup()
