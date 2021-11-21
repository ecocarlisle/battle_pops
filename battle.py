def main():
    player1 = input("State your name PLAYER 1:")
    player2 = input("State your name PLAYER 2:")
    battle(player1)
    battle(player2)


def get_player_moves(player):
    print(player)
    filename = player + '_battle_moves.txt'
    with open(filename, "r") as file:
        all_text = file.read()
        all_text = all_text[:-1]
        player_moves = list(map(str, all_text.split(',')))
    print(len(player_moves))


def battle(player):
    print("Let the battle begin %s!" % player)
    get_player_moves(player)


if __name__ == '__main__':
    main()
