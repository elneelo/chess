class BaseLogic(object):
    @staticmethod
    def board_format_print(board):
        print("")
        for i, row in enumerate(board):
            col_tracker = []
            for j, col in enumerate(row):
                col_tracker.append(" ( " + str(i) + ", " + str(j) + " ) ")
            print(col_tracker)
            print(row)
        print("")

    @staticmethod
    def print_padding(line):
        print("\n" + line + "\n")
