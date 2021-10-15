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

    def set_bet(self, bet):
        self.bet = bet

    def check_bet(self, bet):
        self.set_bet(bet)
        if bet in BetType.bet_types.keys():
            return True
        return False

    def get_bet(self, bet):
        if self.check_bet(bet):
            return BetType.bet_types[bet]

    @staticmethod
    def print_bet():
        for key, value in BetType.bet_types.items():
            print(key, "\t-->\t", value)


# Test
if __name__ == '__main__':
    bet = BetType()
    print(bet.get_bet(3))
    # bet.print_bet()

