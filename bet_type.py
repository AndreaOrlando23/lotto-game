class BetType:
    bet_types = {
        1: "Ambata",
        2: "Ambo",
        3: "Terno",
        4: "Quaterna",
        5: "Cinquina"
    }

    def __init__(self, bet=0):
        self.bet = bet

    def check_bet(self, bet):
        if bet in BetType.bet_types.keys():
            return True
        return False

    def get_bet(self, bet):
        if self.check_bet(bet):
            return BetType.bet_types[bet]

    @staticmethod
    def print_bet():
        print("\nID\tBET\n"+"="*17)
        for key, value in BetType.bet_types.items():
            print(f"|{key}\t{value}")


# Test
if __name__ == '__main__':
    bet = BetType()
    print("Select the number of the bet you want to game with:")
    bet.print_bet()

    test = int(input("\nNumber: "))

    print(bet.get_bet(test))
    print(bet.check_bet(test))

