from city import City
import random


class Extraction:
    extractions = {}

    def __init__(self, num_extracted=5):
        self.num_extracted = num_extracted
    

    def get_extractions(self, cities):
        for city in cities.values():
            # self.extractions[city] = random.sample(range(1, 91), self.num_extracted)
            self.extractions.update({city: random.sample(range(1, 91), self.num_extracted)})
        return self.extractions
    

    def output(self):
        # TODO
        for city, num in self.extractions.items():
            print(city, num)
    




# Test
if __name__ == '__main__':
    cities = City().cities
    extraction = Extraction(5)

    print(extraction.get_extractions(cities))
    print(extraction.output())
