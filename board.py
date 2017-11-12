class ChessBoard:
    # variables
    BOARD_WIDTH = 8
    BOARD_HEIGHT = 8

    def __init__(self):
        self.board = [[None for x in range(ChessBoard.BOARD_WIDTH)] for y in range(ChessBoard.BOARD_HEIGHT)]

    def create_board(self):
        self.pawns_setup()
        self.castles_setup()
        self.bishops_setup()
        self.knights_setup()
        self.queens_setup()
        self.kings_setup()
        self.format_print()

    def format_print(self):
        print("")
        for row in self.board:
            print(row)
        print("")

    def pawns_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 1 or i == 6:
                    self.board[i][j] = 'p'

    def castles_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 or i == 7:
                    if j == 0 or j == 7:
                        self.board[i][j] = 'c'

    def bishops_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 or i == 7:
                    if j == 1 or j == 6:
                        self.board[i][j] = 'b'

    def knights_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 or i == 7:
                    if j == 2 or j == 5:
                        self.board[i][j] = 'kn'

    def queens_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 or i == 7:
                    if j == 3:
                        self.board[i][j] = 'q'

    def kings_setup(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i == 0 or i == 7:
                    if j == 4:
                        self.board[i][j] = 'k'

    def get_board(self):
        return self.board
