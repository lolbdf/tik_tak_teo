# X | O | X
# X | O | O
# O | O | X

run = True


class Player():

    def __init__(self, number, symbol, name):
        self.symbol = symbol
        self.number = number
        self.name = name


class Board:

    def __init__(self):
        self.field = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def convert(self, cell):
        if int(self.field[cell]) == 0:
            return " "
        elif int(self.field[cell]) == 1:
            return "X"
        else:
            return "O"

    def print_board(self):
        print(" " + str(self.convert(0)) + " | " + str(self.convert(1)) + " | " + str(self.convert(2)))
        print(" " + str(self.convert(3)) + " | " + str(self.convert(4)) + " | " + str(self.convert(5)))
        print(" " + str(self.convert(6)) + " | " + str(self.convert(7)) + " | " + str(self.convert(8)))

    def make_moove(self, player):

        while True:
            print(player.name + " ist am Zug. Bitte gib eine Nummer zwischen 1 und 9 ein")
            cell = int(input(">")) - 1

            if self.is_valid_moove(cell):
                self.field[int(cell)] = player.number
                break
            else:
                print(
                    "Dieser Zug war illegal. Bitte achtem sie darauf, das sie eine Zahl zwischen 1 - 9 eingeben, die noch nicht belegt ist!")
                continue

    def is_valid_moove(self, cell):
        if -1 < cell < 9:
            if self.field[int(cell)] == 0:
                return True
        else:
            return False

    def change_turn(self, active_player):
        if active_player == Player1:
            return Player2
        else:
            return Player1

    def check_win(self, active_player):

        if self.field[0] == active_player.number and self.field[1] == active_player.number and self.field[
            2] == active_player.number:
            return True
        elif self.field[3] == active_player.number and self.field[4] == active_player.number and self.field[
            5] == active_player.number:
            return True
        elif self.field[6] == active_player.number and self.field[7] == active_player.number and self.field[
            8] == active_player.number:
            return True

        elif self.field[0] == active_player.number and self.field[4] == active_player.number and self.field[
            8] == active_player.number:
            return True
        elif self.field[2] == active_player.number and self.field[4] == active_player.number and self.field[
            6] == active_player.number:
            return True
        return False

    def board_is_full(self):
        full = True

        for cell in self.field:
            if cell == 0:
                full = False
        return full


if __name__ == "__main__":

    run = True

    while run:
        print("Herzlich Wilkommen zu Tik Tak Toe!")

        print(" 1 | 2 | 3 ")
        print(" 4 | 5 | 6 ")
        print(" 7 | 8 | 9 ")

        print("Bitte geben sie den Namen des Spielers Nummer 1 ein")
        name1 = input(">")

        print("Bitte geben sie den Namen des Spielers Nummer 2 ein")
        name2 = input(">")

        board = Board()

        Player1 = Player(1, "X", name1)
        Player2 = Player(2, "O", name2)

        active_player = Player1

        while True:
            board.make_moove(active_player)

            board.print_board()

            if board.check_win(active_player):

                print(active_player.name + " hat das Spiel gewonnen!")
                print(
                    "Wenn sie direkt noocheinmal spielen wollen geben sie 'JA' ein. Ansonsten wird das Spiel geschlossen.")
                rerun = input(">")
                if rerun == "Ja" or rerun == "ja" or rerun == "JA":
                    run = True
                else:
                    run = False
                break

            if board.board_is_full():
                print("Es sind keine legalen Züge mehr möglich!")
                print(
                    "Wenn sie direkt noocheinmal spielen wollen geben sie 'JA' ein. Ansonsten wird das Spiel geschlossen.")
                rerun = input(">")
                if rerun == "Ja" or rerun == "ja" or rerun == "JA":
                    run = True
                else:
                    run = False
                break

            active_player = board.change_turn(active_player)
