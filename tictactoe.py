class MoveAlreadyMade(Exception):
    def __init__(player):
        super().__init__("move already made")

class TicTacToe:
    def __init__(player):
        player.a = '#'
        player.b = '#'
        player.c = '#'
        player.d = '#'
        player.e = '#'
        player.f = '#'
        player.g = '#'
        player.h = '#'
        player.i = '#'
        player.choice = '#'

    def print_board(player):
        print(f" {player.a} | {player.b} | {player.c}")
        print("---|---|---")
        print(f" {player.d} | {player.e} | {player.f}")
        print("---|---|---")
        print(f" {player.g} | {player.h} | {player.i}")

    def player1_choice(player):
        player.choice = input("enter choice for player 1: ")
        if player.choice == 'a':
            try:
                if player.a != '#':
                    raise MoveAlreadyMade()
                player.a = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'b':
            try:
                if player.b != '#':
                    raise MoveAlreadyMade()
                player.b = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'c':
            try:
                if player.c != '#':
                    raise MoveAlreadyMade()
                player.c = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'd':
            try:
                if player.d != '#':
                    raise MoveAlreadyMade()
                player.d = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'e':
            try:
                if player.e != '#':
                    raise MoveAlreadyMade()
                player.e = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'f':
            try:
                if player.f != '#':
                    raise MoveAlreadyMade()
                player.f = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'g':
            try:
                if player.g != '#':
                    raise MoveAlreadyMade()
                player.g = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'h':
            try:
                if player.h != '#':
                    raise MoveAlreadyMade()
                player.h = 'X'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'i':
            try:
                if player.i != '#':
                    raise MoveAlreadyMade()
                player.i = 'X'
            except MoveAlreadyMade as e:
                print(e)

        player.print_board()

    def player2_choice(player):
        player.choice = input("enter choice for player 2: ")
        if player.choice == 'a':
            try:
                if player.a != '#':
                    raise MoveAlreadyMade()
                player.a = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'b':
            try:
                if player.b != '#':
                    raise MoveAlreadyMade()
                player.b = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'c':
            try:
                if player.c != '#':
                    raise MoveAlreadyMade()
                player.c = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'd':
            try:
                if player.d != '#':
                    raise MoveAlreadyMade()
                player.d = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'e':
            try:
                if player.e != '#':
                    raise MoveAlreadyMade()
                player.e = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'f':
            try:
                if player.f != '#':
                    raise MoveAlreadyMade()
                player.f = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'g':
            try:
                if player.g != '#':
                    raise MoveAlreadyMade()
                player.g = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'h':
            try:
                if player.h != '#':
                    raise MoveAlreadyMade()
                player.h = 'O'
            except MoveAlreadyMade as e:
                print(e)
        elif player.choice == 'i':
            try:
                if player.i != '#':
                    raise MoveAlreadyMade()
                player.i = 'O'
            except MoveAlreadyMade as e:
                print(e)
        
        player.print_board()

    def win(player):
        if (player.a == player.b == player.c == 'X' or player.a == player.d == player.g == 'X' or 
            player.d == player.e == player.f == 'X' or player.g == player.h == player.i == 'X' or 
            player.b == player.e == player.h == 'X' or player.c == player.f == player.i == 'X' or 
            player.a == player.e == player.i == 'X' or player.c == player.e == player.g == 'X'):
            print("player 1 won")
            return False
        elif (player.a == player.b == player.c == 'O' or player.a == player.d == player.g == 'O' or 
              player.d == player.e == player.f == 'O' or player.g == player.h == player.i == 'O' or 
              player.b == player.e == player.h == 'O' or player.c == player.f == player.i == 'O' or 
              player.a == player.e == player.i == 'O' or player.c == player.e == player.g == 'O'):
            print("player 2 won")
            return False
        return True

if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.print_board()
    while tictactoe.win():
        tictactoe.player1_choice()
        if not tictactoe.win():
            break
        tictactoe.player2_choice()
