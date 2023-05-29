
def is_win_bet(bet, extraction):
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
        win_dict = {}
        win_nums = []
        excluded_wheel = [12]  # 12 --> Tutte
        
        for b in bet:
            
            if bet[b]['city'] == 'Tutte':
                cities = {w: cities[w] for w in set(list(cities.keys())) - set(excluded_wheel)}

                for c in cities:
                    for n in bet[b]['nums']:
                        if n in extraction[cities[c]]:
                            win_nums.append(n)

        
            for n in bet[b]['nums']:
                if n in extraction[bet[b]['city']]:
                    win_nums.append(n)   


                if len(win_nums) == bet[b]['bet']:
                    win_dict[b] = {'city': bet[b]['city'], 'bet': bet[b]['bet'], 'nums': win_nums}    
            win_nums = []  # empty the list again for the next ticket (b)

        print(win_dict)
                            
        if bool(win_dict):
            return True, win_dict
        return False, win_dict    


bet = {1: {'city': 'Firenze', 'bet': 3, 'nums': [7, 8, 9]}, 2: {'city': 'Tutte', 'bet': 3, 'nums': [90, 2, 3]}}

extraction = {
        "Bari": [1,2,3],
        "Cagliari": [4,5,6],
        "Firenze": [7,8,9],
        "Genova": [10,11,12],
        "Milano": [13,14,15],
        "Napoli": [16,17,18],
        "Palermo": [19,20,21],
        "Roma": [22,23,24],
        "Torino": [25,26,27],
        "Venezia": [27,28,29],
        "Tutte": [30,31,90]
    }

test = is_win_bet(bet, extraction)

print(test)