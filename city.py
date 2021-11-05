class City:
    """
    City class represents the way to check 
    and retrieve the city name (aka ruota) and
    the relative ID number. It allows the program
    to print out the possible city choice for the user.
    """

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

    def check_city_number(self, number):
        if number in City.cities.keys():
            return True
        return False

    def get_city(self, city):
        if self.check_city_number(city):
            return City.cities[city]

    @staticmethod
    def print_cities():
        print("\nID\tCITY\n"+"="*17)
        for key, value in City.cities.items():
            print(f"|{key}\t{value}")
    


# Test
if __name__ == '__main__':
    city = City()
    print("Select the number of the city you want to game with:")
    city.print_cities()
        
    test = int(input("\nNumber: "))
    print(city.get_city(test))
    print(city.check_city_number(test))

