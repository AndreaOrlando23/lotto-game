from lotto.city import City
import random


class Extraction:
    extractions = {}

    def __init__(self, num_extracted=5):
        self.num_extracted = num_extracted
    

    def get_extractions(self, cities):
        for city in cities.values():
            self.extractions.update({city: random.sample(range(1, 91), self.num_extracted)})
        return self.extractions
    
    
    def output(self):
        table_line = '+'+'='*48+'+'
        print(table_line)
        print('|', 'CITY'.center(10), '|{:^35}|'.format(' '.join('NUMBERS')))
        print(table_line)
        base_line = '+'+'-'*48+'+'
        
        for city in self.extractions.keys():
            print('|', city.center(10), '|{:^35}|'.format('  '.join([str(nums) for nums in self.extractions[city]])))
            print(base_line)




# Test
if __name__ == '__main__':
    cities = City().cities
    extraction = Extraction(5)

    extraction.get_extractions(cities)
    extraction.output()
