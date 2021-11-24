import random


def main():
    try:
        print("Let the battle begin %s!")
        player1 = "FartMomz"
        player2 = "PurpleNurple"
        battle(player1)
        battle(player2)
    except Exception as e:
        print("error in main routine:", e.args)


def get_player_move_files(player):
    file_dir = "battle_moves/"
    filename = file_dir + player + '_battle_moves.txt'
    print(filename)
    with open(filename, "r") as file:
        all_text = file.read()
        all_text = all_text[:-1]
        player_moves = list(map(str, all_text.split('\n')))

    whole_number = random.randint(0, 4)
    print(player, whole_number, player_moves[whole_number])


def battle(player):
    get_player_move_files(player)


if __name__ == '__main__':
    main()
