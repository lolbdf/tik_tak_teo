import random

# X | O | X
# X | O | O
# O | O | X

#    0  1  2  3
#    4  5  6  7
#    8  9 10 11
#   12 13 14 15

run = True


class AI:
    ai = True
    number = 2
    symbol = "X"


class Player:
    ai = False

    def __init__(self, number, symbol, name):
        self.symbol = symbol
        self.number = number
        self.name = name


class Board:

    def __init__(self, field_size=9):
        self.field = [0] * field_size
        self.field_size = field_size

    def convert(self, cell):
        if int(self.field[cell]) == 0:
            return " "
        elif int(self.field[cell]) == 1:
            return "X"
        else:
            return "O"

    def print_board(self):
        if int(self.field_size) == 9:
            print(" " + str(self.convert(0)) + " | " + str(self.convert(1)) + " | " + str(self.convert(2)))
            print(" " + str(self.convert(3)) + " | " + str(self.convert(4)) + " | " + str(self.convert(5)))
            print(" " + str(self.convert(6)) + " | " + str(self.convert(7)) + " | " + str(self.convert(8)))

        elif int(self.field_size) == 16:
            print(
                " " + str(self.convert(0)) + " | " + str(self.convert(1)) + " | " + str(self.convert(2)) + " | " + str(
                    self.convert(3)))
            print(
                " " + str(self.convert(4)) + " | " + str(self.convert(5)) + " | " + str(self.convert(6)) + " | " + str(
                    self.convert(7)))
            print(
                " " + str(self.convert(8)) + " | " + str(self.convert(9)) + " | " + str(self.convert(10)) + " | " + str(
                    self.convert(11)))
            print(" " + str(self.convert(12)) + " | " + str(self.convert(13)) + " | " + str(
                self.convert(14)) + " | " + str(self.convert(15)))
        else:
            pass

    def make_moove(self, player):

        if not player.ai:
            while True:
                print(player.name + " ist am Zug. Bitte gib eine Ganzzahl von 1 - " + str(self.field_size) + " ein")

                cell = input(">")

                if self.is_valid_moove(cell):
                    cell = int(cell) - 1
                    self.field[int(cell)] = player.number
                    break
                else:
                    print(
                        "Dieser Zug war illegal. Bitte achtem sie darauf, das sie eine GANZZAHL von 1 - " + str(
                            self.field_size) + " eingeben, die noch nicht belegt ist!")
                    continue
        else:
            while True:
                cell = random.randint(0, self.field_size -1)
                if self.field[cell] == 0:
                    self.field[int(cell)] = player.number
                    break


    def is_valid_moove(self, cell):
        try:
            cell = int(cell) - 1
            if -1 < cell < self.field_size:
                if self.field[cell] == 0:
                    return True
            else:
                return False
        except ValueError:
            return False
        except TypeError:
            return False

    def change_turn(self, active_player):
        if active_player == Player1:
            return Player2
        else:
            return Player1

    def check_win(self, active_player):

        if self.field_size == 9:
            if self.field[0] == active_player.number and self.field[1] == active_player.number and self.field[
                2] == active_player.number:
                return True
            elif self.field[3] == active_player.number and self.field[4] == active_player.number and self.field[
                5] == active_player.number:
                return True
            elif self.field[6] == active_player.number and self.field[7] == active_player.number and self.field[
                8] == active_player.number:
                return True

            elif self.field[0] == active_player.number and self.field[3] == active_player.number and self.field[
                6] == active_player.number:
                return True
            elif self.field[1] == active_player.number and self.field[4] == active_player.number and self.field[
                7] == active_player.number:
                return True
            elif self.field[2] == active_player.number and self.field[5] == active_player.number and self.field[
                8] == active_player.number:
                return True

            elif self.field[0] == active_player.number and self.field[4] == active_player.number and self.field[
                8] == active_player.number:
                return True
            elif self.field[2] == active_player.number and self.field[4] == active_player.number and self.field[
                6] == active_player.number:
                return True
            return False
        elif self.field_size == 16:
            if self.field[0] == active_player.number and self.field[1] == active_player.number and self.field[
                2] == active_player.number and self.field[3] == active_player.number:
                return True
            elif self.field[4] == active_player.number and self.field[5] == active_player.number and self.field[
                6] == active_player.number and self.field[7] == active_player.number:
                return True
            elif self.field[8] == active_player.number and self.field[9] == active_player.number and self.field[
                10] == active_player.number and self.field[11] == active_player.number:
                return True
            elif self.field[12] == active_player.number and self.field[13] == active_player.number and self.field[
                14] == active_player.number and self.field[15] == active_player.number:
                return True

            elif self.field[0] == active_player.number and self.field[4] == active_player.number and self.field[
                8] == active_player.number and self.field[12] == active_player.number:
                return True
            elif self.field[1] == active_player.number and self.field[5] == active_player.number and self.field[
                9] == active_player.number and self.field[13] == active_player.number:
                return True
            elif self.field[2] == active_player.number and self.field[6] == active_player.number and self.field[
                10] == active_player.number and self.field[14] == active_player.number:
                return True
            elif self.field[3] == active_player.number and self.field[7] == active_player.number and self.field[
                11] == active_player.number and self.field[15] == active_player.number:
                return True

            elif self.field[0] == active_player.number and self.field[5] == active_player.number and self.field[
                10] == active_player.number and self.field[15] == active_player.number:
                return True
            elif self.field[3] == active_player.number and self.field[6] == active_player.number and self.field[
                9] == active_player.number and self.field[12] == active_player.number:
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
        print()
        print("Bitte suchen sie sich eine Spielfeldgröße aus.")
        print("Zur Auswahl steht die Feldgröße 3 x 3 ")
        print("")
        print("Feld1:")
        print("")
        print(" 1 | 2 | 3 ")
        print(" 4 | 5 | 6 ")
        print(" 7 | 8 | 9 ")
        print("")
        print("")
        print("Oder die Feldgröße 4 x 4 :")
        print("")
        print("Feld2:")
        print("")
        print("  1 |  2 |  3 |  4 ")
        print("  5 |  6 |  7 |  8 ")
        print("  9 | 10 | 11 | 12 ")
        print(" 13 | 14 | 15 | 16 ")

        while True:
            try:
                print()
                print()
                print()
                print(
                    "Bitte geben sie 'Feld1' ein wenn sie mit 3 x 3 Feldern spielen möchten oder 'Feld2' wenn sie mit 4 x 4 spielen möchten")
                field_size = input(">")
                if field_size == "Feld1":
                    field_size = 9
                    break
                elif field_size == "Feld2":
                    field_size = 16
                    break
                else:
                    print()
                    print()
                    print("Das ist eine Pflichteingabe! Bitte achten sie auf eine korrekte Schreibweise")
            except ValueError:
                print()
                print()
                print("Das ist eine Pflichteingabe! Bitte achten sie auf eine korrekte Schreibweise")

        print()
        print()
        print(
            "Wie immer gewinnt derjenige, der zuerst eine Diagonale, Senkrechte oder Wagerechte mit seinem Zeichen besetzt.")
        print()
        print()

        while True:
            print()
            print()
            print("möchten sie gegen die AI (1) oder einen anderen Spieler (2) spielen?")
            opponent = input(">")
            if opponent == "1" or opponent == "2":
                break
            print()
            print()
            print(
                "Das ist eine Pflichteingabe! Bitte geben sie entweder die 1 für ein Spiel gegen die AI ein oder eine 2 wenn sie gegen einen anderen Menschen spielen möchten!")

        if int(opponent) == 1:
            print("Bitte geben sie ihren Namen ein")
            name1 = input(">")
            Player1 = Player(1, "X", name1)

            Player2 = AI()

        else:
            print("Bitte geben sie den Namen des Spielers Nummer 1 ein")
            name1 = input(">")
            Player1 = Player(1, "X", name1)

            print("Bitte geben sie den Namen des Spielers Nummer 2 ein")
            name2 = input(">")
            Player2 = Player(2, "O", name2)

        board = Board(field_size)

        active_player = Player1

        print()
        board.print_board()

        while True:
            print()
            board.make_moove(active_player)
            print()
            board.print_board()
            print()

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
