# Lotto Game
#### [TomorrowDevs](https://github.com/AndreaOrlando23/programming-basics/tree/main/projects/m6/001-lotto-game) - Learning Path 1

___
## Requirements
- This program simulate the Italian [Lotto Game](https://it.wikipedia.org/wiki/Lotto)
- The project is implemented using OOP so that it can be extended in the next learning path
- The software parse the user input to generate tickets (min: 1, max: 5) and start the gane (0: exit)
- For each bill the software ask the type of bill (ambata, ambo, terno, quaterna, cinquina) and the amount of numbers to generate (max 10 per bill) and the "city" (aka "ruota") of the bill: Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia and Tutte
- Numbers will be randomly generated in the range 1-90 (inclusive)
- Generate the ticket with nice ascii art table [decoration](https://ozh.github.io/ascii-tables/)

___
## Classes & Methods of lotto package

`Lotto`
- `tickets_generator()` - loop for each bill and return information tickets
- `quit_program(istruction)` - quit the program with specific istruction
- `get_city_name(n_ticket)` - get city name for each bill
- `get_bet_type(n_ticket)` - get bet type for each bill
- `get_bet_id(value)` - get bet id for each bill (need for check)
- `get_nums(n_ticket, bet_type, bet_id)` - get nums for each bill
- `numbers_generator(numbers)` - return list of numbers randomly generated in the range 1-90 (inclusive)
- `loading_bar()` - build a fancy loading bar

`Bet`
- `check_bet(bet)` - check if the bet passed is in `Bet.bet_types{}`
- `get_bet(bet)` - return value pick by key passed
- `print_bet()` - @staticmethod that print out key and values from `Bet.bet_types{}`

`City`
- `check_city_number(number)` - check if the bet passed is in `Bet.bet_types{}`
- `get_city(city)` - return value picked by key passed
- `print_cities()` - @staticmethod that print out key and values from `City.cities{}`

___
## How to Play
From CLI, enter the following command:

`$ python3 main.py -n <int>`

Where `<int>` must be replaced with integer value (min: 1, max: 5)

If you need to see more information about the rules of Lotto Game program, then enter the following command:

`$ python3 main.py -v`

___
## Output
The program is designed to render an ascii style representation of ***n*** lotto tickets, as the following output sample:

```Python
"""
Expected Output:
+================================================+
|                  TICKET <n>                    |
|------------------------------------------------|
|                 City: <city_name>              |
|                 Bet: <bet_type>                |
|               <numbers_extracted>              |
+================================================+
"""
```
