from city import City
from bet import Bet
from ticket import Ticket
import random


class Lotto:

    def __init__(self, num_tickets):
        self.num_tickets = num_tickets
        self.tickets = []


    def tickets_generator(self):
        decorator = '='*50

        for betting in range(self.num_tickets):
            print(decorator)
            print('{:^50}'.format(f'### TICKET {betting+1} ###'))
            print(decorator)

            
            city = self.get_city_id(betting+1)
            while city == False:
                city = self.get_city_id(betting+1)
            

            bet = self.get_bet_id(betting+1)
            while bet == False:
                bet = self.get_bet_id(betting+1)

            """
            c = City()
            c.print_cities()
            pick_city = int(input(f"\n>>> TICKET {betting+1} - Enter City ID: "))
            if c.check_city_number(pick_city):
                city = c.get_city(pick_city)
            else:
                print(f"\nERROR: {pick_city} is not a valid City ID. Please try again.")
                pick_city = int(input(f"\n>>> TICKET {betting+1} - Enter City ID: "))
                city = c.get_city(pick_city)
            

            b = Bet()
            b.print_bet()
            pick_bet = int(input(f"\n>>> TICKET {betting+1} - Enter Bet Type ID: "))
            if b.check_bet(pick_bet):
                bet = b.get_bet(pick_bet)
            else:
                print(f"\nERROR: {pick_bet} is not a valid Bet Type ID. Please try again.")
                pick_bet = int(input(f"\n>>> TICKET {betting+1} - Enter Bet Type ID: "))
                bet = b.get_bet(pick_bet)
            """

            extraction = self.numbers_generator(5)

            ticket = Ticket(betting+1, self.num_tickets, city, bet, extraction)
            self.tickets.append(ticket)
        
        for ticket in self.tickets:
            print(ticket.print_ticket())

        
    def get_city_id(self, n_ticket):
        c = City()
        c.print_cities()
        city_id = input(f"\n>>> TICKET {n_ticket} - Enter City ID: ")
        try:
            city_name = int(city_id)
            if c.check_city_number(city_name):
                city = c.get_city(city_name)
                return city
            print(f'\nERROR: "{city_id}" is not a valid City ID.\nPlease choose from the following table:')
            return False
        except:
            print(f'\nERROR: "{city_id}" is not a valid City ID.\nPlease choose from the following table:')
            return False
    

    def get_bet_id(self, n_ticket):
        b = Bet()
        b.print_bet()
        bet_id = input(f"\n>>> TICKET {n_ticket} - Enter City ID: ")
        try:
            bet_type = int(bet_id)
            if b.check_bet(bet_type):
                bet = b.get_bet(bet_type)
                return bet
            print(f'\nERROR: "{bet_id}" is not a valid Bet Type ID.\nPlease choose from the following table:')
            return False
        except:
            print(f'\nERROR: "{bet_id}" is not a valid Bet Type ID.\nPlease choose from the following table:')
            return False


    def numbers_generator(self, numbers):
        extraction = random.sample(range(1, 91), int(numbers))
        return extraction  # type list()




# Test

if __name__ == '__main__':
    lotto = Lotto(3)

    lotto.tickets_generator()

    
        











"""
class Lotto:
    def __init__(self, city=0, bet=0, numbers=0):
        self.city = city
        self.bet = bet
        self.numbers = numbers

    def pick_city(self):
        print("> Pick the 'ruota' (aka city) by the corresponding number:")
        City.print_cities()

        city = int(input("> Enter the corresponding number of the city: "))
        c = City(city)
        if c.get_city(city):
            self.city = c.get_city(city)
            return self.city
        else:
            return "Enter a number between 1 to 12"

    def pick_bet(self):
        print("> Pick the bet type by the corresponding number:")
        BetType.print_bet()

        bet = int(input("> Enter the corresponding number of the bet type: "))
        b = BetType(bet)
        if b.get_bet(bet):
            self.bet = b.get_bet(bet)
            return self.bet
        else:
            return "Enter a number between 1 to 5"

        '''
        if City.check_city(city):
            c = City(city)
            self.city = c.get_city(city)
        
        else:
            print("Enter a number between 1 to 12")
        '''


lotto = Lotto()
print(lotto.pick_city())
print(lotto.pick_bet())
"""
