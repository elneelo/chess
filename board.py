class ChessBoard:
    # variables
    BOARD_WIDTH = 8
    BOARD_HEIGHT = 8
    PLAYER_ONE_INDICATOR = '_PL1'
    PLAYER_TWO_INDICATOR = '_PL2'

    INDICATOR_LIST = [PLAYER_ONE_INDICATOR, PLAYER_TWO_INDICATOR]

    PAWN = '__pawn'
    CASTLE = 'castle'
    BISHOP = 'bishop'
    KNIGHT = 'knight'
    QUEEN = '_queen'
    KING = '__king'
    EMPTY_TILE = '___EMPTY__'

    def __init__(self):
        self.indicator = None
        self.board = [[
            ChessBoard.EMPTY_TILE for x in range(ChessBoard.BOARD_WIDTH)] for y in range(ChessBoard.BOARD_HEIGHT)]

    def create_board(self):
        for indicator in ChessBoard.INDICATOR_LIST:
            self.indicator = indicator
            self.pawns_setup()
            self.castles_setup()
            self.bishops_setup()
            self.knights_setup()
            self.queens_setup()
            self.kings_setup()
        self.format_print()

    def format_print(self):
        print("")
        for i, row in enumerate(self.board):
            col_tracker = []
            for j, col in enumerate(row):
                col_tracker.append(" ( " + str(i) + ", " + str(j) + " ) ")
            print(col_tracker)
            print(row)
        print("")

    def pawns_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 1 and self.indicator == ChessBoard.PLAYER_ONE_INDICATOR:
                    self.board[i][j] = ChessBoard.PAWN + self.indicator
                elif i == 6 and self.indicator == ChessBoard.PLAYER_TWO_INDICATOR:
                    self.board[i][j] = ChessBoard.PAWN + self.indicator

    def castles_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 and self.indicator == ChessBoard.PLAYER_ONE_INDICATOR:
                    if j == 0 or j == 7:
                        self.board[i][j] = ChessBoard.CASTLE + self.indicator
                elif i == 7 and self.indicator == ChessBoard.PLAYER_TWO_INDICATOR:
                    if j == 0 or j == 7:
                        self.board[i][j] = ChessBoard.CASTLE + self.indicator

    def bishops_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 and self.indicator == ChessBoard.PLAYER_ONE_INDICATOR:
                    if j == 1 or j == 6:
                        self.board[i][j] = ChessBoard.BISHOP + self.indicator
                if i == 7 and self.indicator == ChessBoard.PLAYER_TWO_INDICATOR:
                    if j == 1 or j == 6:
                        self.board[i][j] = ChessBoard.BISHOP + self.indicator

    def knights_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 and self.indicator == ChessBoard.PLAYER_ONE_INDICATOR:
                    if j == 2 or j == 5:
                        self.board[i][j] = ChessBoard.KNIGHT + self.indicator
                elif i == 7 and self.indicator == ChessBoard.PLAYER_TWO_INDICATOR:
                    if j == 2 or j == 5:
                        self.board[i][j] = ChessBoard.KNIGHT + self.indicator

    def queens_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 and self.indicator == ChessBoard.PLAYER_ONE_INDICATOR:
                    if j == 3:
                        self.board[i][j] = ChessBoard.QUEEN + self.indicator
                elif i == 7 and self.indicator == ChessBoard.PLAYER_TWO_INDICATOR:
                    if j == 3:
                        self.board[i][j] = ChessBoard.QUEEN + self.indicator

    def kings_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 and self.indicator == ChessBoard.PLAYER_ONE_INDICATOR:
                    if j == 4:
                        self.board[i][j] = ChessBoard.KING + self.indicator
                elif i == 7 and self.indicator == ChessBoard.PLAYER_TWO_INDICATOR:
                    if j == 4:
                        self.board[i][j] = ChessBoard.KING + self.indicator

    def get_board(self):
        return self.board
