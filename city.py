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

    def city_check(self):
        if self.__city in City.cities.keys():
            return True
        return False

    def set_city(self, city):
        self.__city = city

    def get_city(self, city):
        self.__city = city
        if self.city_check():
            return City.cities[city]

    @staticmethod
    def print_cities():
        for key, value in City.cities.items():
            print(key, value)


# Test
city = City()
print(city.get_city(3))
city.print_cities()
