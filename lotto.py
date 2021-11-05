import time
import sys
import random
from city import City
from bet import Bet
from ticket import Ticket


class Lotto:
    """
    Lotto class represents the business logic of the program.
    The methods process all the inputs from the user and manage controls flow.
    If the input pass all the controls, the program will print out the tickets 
    with all the information needed.
    """

    def __init__(self, num_tickets):
        self.num_tickets = num_tickets
        self.tickets = []


    def tickets_generator(self):
        decorator = '='*50

        for betting in range(self.num_tickets):
            print(decorator)
            print('{:^50}'.format(f'### TICKET {betting+1} ###'))
            print(decorator)

            
            city = self.get_city_name(betting+1)
            while city == False:
                city = self.get_city_name(betting+1)

            bet_type = self.get_bet_type(betting+1)
            while bet_type == False:
                bet_type = self.get_bet_type(betting+1)
            
            bet_id = self.get_bet_id(bet_type)  # return bet id

            nums = self.get_nums(betting+1, bet_type, bet_id)
            while nums == False:
                nums = self.get_nums(betting+1, bet_type, bet_id)
            
            extraction = self.numbers_generator(nums)

            ticket = Ticket(betting+1, self.num_tickets, city, bet_type, extraction)
            self.tickets.append(ticket)
        
        print("\nTickets Processing ...\n")
        
        self.loading_bar()
    

        print("\n" + decorator)
        print('{:^50}'.format(f'### HERE YOUR {self.num_tickets} TICKETS ###'))
        print(decorator)
        
        for ticket in self.tickets:
            print(ticket.print_ticket())
        
        print(decorator)
        print('{:^50}'.format('GOOD LUCK ;)'))
        print(decorator)


    def quit_program(self, istruction):
        if int(istruction) == 0:
            print("\nQuitting program ...\n")
            quit()
        return False
    
        
    def get_city_name(self, n_ticket):
        c = City()
        c.print_cities()
        ask_city_id = input(f"\n>>> TICKET {n_ticket} - Enter City ID aka Ruota: ")
        try:
            id = int(ask_city_id)
            if c.check_city(id):
                city_name = c.get_city(id)
                return city_name
            print(f'\nERROR: "{ask_city_id}" is not a valid City ID.\nPlease choose from the following table:')
            return False
        except:
            print(f'\nERROR: "{ask_city_id}" is not a valid City ID.\nPlease choose from the following table:')
            return False
    

    def get_bet_type(self, n_ticket):
        b = Bet()
        b.print_bet()
        ask_bet_id = input(f"\n>>> TICKET {n_ticket} - Enter Bet Type ID: ")
        try:
            id = int(ask_bet_id)
            if b.check_bet(id):
                bet_type = b.get_bet(id)
                return bet_type
            print(f'\nERROR: "{ask_bet_id}" is not a valid Bet Type ID.\nPlease choose from the following table:')
            return False
        except:
            print(f'\nERROR: "{ask_bet_id}" is not a valid Bet Type ID.\nPlease choose from the following table:')
            return False
    

    def get_bet_id(self, value):
        """
        This method is useful for managing and controls
        the user input when the numbers choosen from the user
        are lower then the bet type choose previously
        """
        for id, val in Bet().bet_types.items():
            if val == value:
                return id
    
    
    def get_nums(self, n_ticket, bet_type, bet_id):
        ask_nums = input(f"\n>>> How many numbers you want bet for TICKET {n_ticket} [min 1 | max 10]: ")
        try:
            nums = int(ask_nums)
            if 1 <= nums <= 10:
                if nums >= bet_id:
                    return nums
                print(f'\nERROR: You have entered to few numbers ({nums}) for your type of bet ({bet_type}). Please try again.')
                return False
            print(f'\nERROR: "{ask_nums}" is not a valid Bet Type ID [min 1 | max 10]. Please try again.')
            return False
        except:
            print(f'\nERROR: "{ask_nums}" is not a valid Bet Type ID [min 1 | max 10]. Please try again.')
            return False


    def numbers_generator(self, numbers):
        extraction = random.sample(range(1, 91), int(numbers))
        return extraction  # type list()
    

    def loading_bar(self):
        for i in range(21):
            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
            sys.stdout.flush()
            time.sleep(0.05)
        print()


# Test
if __name__ == '__main__':
    lotto = Lotto(1)
    lotto.tickets_generator()
