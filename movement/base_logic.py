class BaseLogic(object):
    @staticmethod
    def board_format_print(board):
        print("")
        for row in board:
            print(row)
        print("")

    @staticmethod
    def print_padding(line):
        print("\n" + line + "\n")
