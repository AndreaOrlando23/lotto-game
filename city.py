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
        self.__city = city

    def set_city(self, city):
        self.__city = city

    def check_city(self, city):
        self.set_city(city)
        if city in City.cities.keys():
            return True
        return False

    def get_city(self, city):
        if self.check_city(city):
            return City.cities[city]

    @staticmethod
    def print_cities():
        for key, value in City.cities.items():
            print(key, "\t-->\t", value)


# Test
if __name__ == '__main__':
    city = City()
    test = int(input("Number: "))
    print(city.get_city(test))
    # city.print_cities()

