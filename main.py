# Entry point: ask how many tickets he want to create - from 1 to 5
import argparse
from lotto import Lotto


def main():

    
    parser = argparse.ArgumentParser(prog='TICKET')
    parser.add_argument('-n', type = int, help='num ticket from 1 to 5', choices= [1, 2, 3, 4, 5])
    args = parser.parse_args()
    num_of_tickets = vars(args)
    lotto = Lotto(num_of_tickets['n'])
    generate_ticket = lotto.tickets_generator()


if __name__ == '__main__':
    main()