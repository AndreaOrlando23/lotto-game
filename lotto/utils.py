LOTTO_GAME_RULES = """
========================================
### RULES OF LOTTO GAME -- LEVEL LP2 ###
========================================

1. Entry point: choose num of tickets with the following command (CLI)

    $ python3 main.py -n <int>  (<int> must be min: 1, max: 5, 0: exit)

2. For each bill the software ask the "city" (aka "ruota") of the bill: 
    Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia and Tutte.

3. For each bill the software ask the type of bill (ambata, ambo, terno, quaterna, cinquina) and the amount of numbers to generate (max 10 per bill).

4. Numbers will be randomly generated in the range 1-90 (inclusive).

5. Once all the information are stored, the software will:
    - print out the tickets
    - print out the global lotto extraction
    - check if there are winning ticket
    - output the result
    - in case of win, print out winning tickets (with evidence on winning numbers)

========================================
### ENJOY YOUR GAME AND GOOD LUCK ;) ###
========================================
"""
