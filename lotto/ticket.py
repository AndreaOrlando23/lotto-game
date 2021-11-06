from lotto.city import City
from lotto.bet import Bet


class Ticket:

    """
    Ticket class represents the ticket format build for
    the Lotto Game program.

    Expected Output:
    +================================================+
    |                  TICKET <n>                    |
    |------------------------------------------------|
    |                 City: <city_name>              |
    |                 Bet: <bet_type>                |
    |               <numbers_extracted>              |
    +================================================+
    """

    def __init__(self, id_ticket, num_tickets, city, bet, num_extracted=[]):
        self.id_ticket = id_ticket
        self.num_tickets = num_tickets
        self.city = city
        self.bet = bet
        self.num_extracted = num_extracted

    def print_ticket(self):
        table_line = '+'+'='*48+'+'
        table_midline = '|'+'-'*48+'|'
        header = '|{:^48}|'.format('TICKET ' + str(self.id_ticket))
        city = '|{:^48}|'.format('City: ' + self.city)
        bet = '|{:^48}|'.format('Bet: ' + self.bet)
        numbers = '|{:^48}|'.format(' '.join([str(elem) for elem in self.num_extracted]))
        


        return f"""
{table_line}
{header}
{table_midline}
{city}
{bet}
{numbers}
{table_line}
        """


# Test
if __name__ == '__main__':
    city = City()
    print("Select the number of the city you want to game with:")
    city.print_cities()
        
    test_city = int(input("Number: "))
    get_city = city.get_city(test_city)
    

    bet = Bet()
    print("Select the number of the bet you want to game with:")
    bet.print_bet()

    test_bet = int(input("Number: "))
    get_bet = bet.get_bet(test_bet)

    ticket = Ticket(1, 1, get_city, get_bet, [1, 2, 3, 4, 5])
    print(ticket.print_ticket())


