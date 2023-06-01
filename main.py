import argparse
from lotto.ticket import Ticket
from lotto.lotto import Lotto
from lotto.utils import LOTTO_GAME_RULES


def main():
    parser = argparse.ArgumentParser(description='LOTTO GAME')
    parser.add_argument('-n', '-numtickets', type = int, help='num tickets from 1 to 5', choices= [1, 2, 3, 4, 5])
    parser.add_argument('-v', '-verbose', help='Rules of Lotto Game', action='store_true')
    args = parser.parse_args()
    data = vars(args)
    
    if data['v']:
        print(LOTTO_GAME_RULES)

    if data['n']:
        Ticket.print_decorator('### LOTTO GAME ###')

        print(f"\nYou have choose to play with {data['n']} Tickets.\n")
        point_check = input("Press any key to start the game! (press 0 to quit) ")
        if point_check == "0":
            Lotto(data['n']).quit_program(point_check)

        lotto = Lotto(data['n'])
        generate_ticket = lotto.extractions_manager()  # the name was tickets_generator() in the previous branch (learning_path_1)


if __name__ == '__main__':
    main()