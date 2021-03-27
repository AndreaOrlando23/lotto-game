from city import City
from bet_type import BetType


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
