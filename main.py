import argparse
from lotto import Lotto
import utils


def main():
    parser = argparse.ArgumentParser(description='LOTTO GAME')
    parser.add_argument('-n', '-numtickets', type = int, help='num tickets from 1 to 5', choices= [1, 2, 3, 4, 5])
    parser.add_argument('-v', '-verbose', help='Rules of Lotto Game', action='store_true')
    args = parser.parse_args()
    data = vars(args)
    
    if data['v']:
        print(utils.LOTTO_GAME_RULES)

    if data['n']:
        print(utils.DECORATOR)
        print('{:^50}'.format('### LOTTO GAME ###'))
        print(utils.DECORATOR)

        print(f"\nYou have choose to play with {data['n']} Tickets.\n")
        point_check = input("Press any key to start the game! (press 0 to quit) ")
        if point_check == "0":
            Lotto(data['n']).quit_program(point_check)

        lotto = Lotto(data['n'])
        generate_ticket = lotto.tickets_generator()


if __name__ == '__main__':
    main()