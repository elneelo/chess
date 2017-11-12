from board import ChessBoard
from movement.pawn_movement_logic import PawnMovementLogic


def game_setup():
    chess_board = ChessBoard()
    chess_board.create_board()
    # print(chess_board.get_board())
    move = PawnMovementLogic(chess_board.get_board(), 1, 2, 3, 2, ChessBoard.PLAYER_ONE_INDICATOR, True)
    move.move_pawn()
    move = PawnMovementLogic(chess_board.get_board(), 6, 3, 5, 3, ChessBoard.PLAYER_TWO_INDICATOR, True)
    move.move_pawn()
    move = PawnMovementLogic(chess_board.get_board(), 3, 2, 4, 2, ChessBoard.PLAYER_ONE_INDICATOR, False)
    move.move_pawn()
    print("here_1")
    move = PawnMovementLogic(chess_board.get_board(), 5, 3, 4, 2, ChessBoard.PLAYER_TWO_INDICATOR, False)
    move.capture_piece()


game_setup()
