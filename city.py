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

    def set_city(self, city):
        self.city = city

    def check_city_number(self, number):
        # self.set_city(city)
        if number in City.cities.keys():
            return True
        return False

    def get_city(self, city):
        if self.check_city_number(city):
            return City.cities[city]

    @staticmethod
    def print_cities():
        for key, value in City.cities.items():
            print(f"{key} - {value}")


# Test
if __name__ == '__main__':
    city = City()
    print("Select the number of the city you want to game with:")
    city.print_cities()
        
    test = int(input("Number: "))
    print(city.get_city(test))
    # city.print_cities()

