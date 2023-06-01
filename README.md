# Lotto Game
#### TomorrowDevs - [Learning Path 2](https://github.com/AndreaOrlando23/programming-basics/tree/main/projects/m6/002-lotto-fake-extraction)

___
## Requirements
- This program simulate the Italian [Lotto Game](https://it.wikipedia.org/wiki/Lotto)
- The project is implemented using OOP so that it can be extended in the next learning path
- The software parse the user input to generate tickets (min: 1, max: 5) and start the gane (0: exit)
- For each bill the software ask the type of bill (ambata, ambo, terno, quaterna, cinquina) and the amount of numbers to generate (max 10 per bill) and the "city" (aka "wheel") of the bill: Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia and Tutte
- Numbers will be randomly generated in the range 1-90 (inclusive)
- Generate the ticket with nice ascii art table [decoration](https://ozh.github.io/ascii-tables/)
- Generate lotto extraction based on cities (aka "wheel")

___
## Classes & Methods of lotto package

`Lotto`
- `extractions_manager()` - loop for each bill and return tickets and lotto information (ex `tickets_generator()`)
- `is_win_bet()` - check if the bet win on lotto extraction
- `quit_program(istruction)` - quit the program with specific istruction
- `get_city_name(n_ticket)` - get city name for each bill
- `get_bet_type(n_ticket)` - get bet type for each bill
- `get_bet_id(value)` - get bet id for each bill (need for check)
- `get_nums(n_ticket, bet_type, bet_id)` - get nums for each bill
- `numbers_generator(numbers)` - return list of numbers randomly generated in the range 1-90 (inclusive)
- `loading_bar()` - build a fancy loading bar

`Bet`
- `check_bet(bet int)` - check if the bet passed is in `Bet.bet_types{}`
- `get_bet(bet int)` - return value pick by key passed
- `print_bet()` - @staticmethod that print out key and values from `Bet.bet_types{}`

`City`
- `check_city(id int)` - check if the bet passed is in `Bet.bet_types{}`
- `get_city(city int)` - return value picked by key passed
- `print_cities()` - @staticmethod that print out key and values from `City.cities{}`

`Ticket`
- `get_tickets(id int, city string, bet_id int, bet_type string, nums list)` - generate dict with information passed
- `print_ticket()` - return and print all tickets in ascii style
- `print_decorator()` - @staticmethod that print out an ascii decorator
- `you_win()` - @staticmethod that print out an ascii decorator

`Extraction`
- `get_extractions(cities dict)` - return dict with city as key and list of nums as value
- `output()` - print out lotto extraction in ascii style

`Extraction`

Is only a set of verbose information on lotto game (see next section)

___
## How to Play
From CLI, enter the following command:

`$ python3 main.py -n <int>`

Where `<int>` must be replaced with integer value (min: 1, max: 5)

If you need to see more information about the rules of Lotto Game program, then enter the following command:

`$ python3 main.py -v`

___
## Output
The program is designed to render an ascii style representation of ***n*** lotto tickets and lotto extraction, as the following output sample:

```Python

Expected Output:
+================================================+
|                  TICKET <n>                    |
|------------------------------------------------|
|                 City: <city_name>              |
|                 Bet: <bet_type>                |
|               <numbers_extracted>              |
+================================================+

+================================================+
|    CITY    |           N U M B E R S           |
+================================================+
|    Bari    |         84  39  9  71  65         |
+------------------------------------------------+
|  Cagliari  |         4  34  9  87  28          |
+------------------------------------------------+
|  Firenze   |        83  47  46  72  25         |
+------------------------------------------------+
|   Genova   |        55  40  66  17  72         |
+------------------------------------------------+
|   Milano   |        89  54  21  18  71         |
+------------------------------------------------+
|   Napoli   |        26  32  50  61  44         |
+------------------------------------------------+
|  Palermo   |        27  63  77  85  14         |
+------------------------------------------------+
|    Roma    |          1  7  6  19  21          |
+------------------------------------------------+
|   Torino   |         8  57  2  14  36          |
+------------------------------------------------+
|  Venezia   |         32  30  52  79  6         |
+------------------------------------------------+
|   Tutte    |         19  72  2  90  66         |
+------------------------------------------------+

```

## `Play your game and good luck! :-)`