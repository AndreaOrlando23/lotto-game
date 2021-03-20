class City:
    cities = {
        1: "Bari",
        2: "Cagliari",
        3: "Firenze",
        4: "Genova",
        5: "Milano",
        6: "Napoli",
        8: "Palermo",
        9: "Roma",
        10: "Torino",
        11: "Venezia",
        12: "Tutte"
    }

    def __init__(self, city=0):
        self.city = city

    def city_check(self):
        if self.city in City.cities.keys():
            return True
        return False

    @staticmethod
    def print_cities():
        for key, value in City.cities.items():
            print(key, value)

