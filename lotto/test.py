my_dict = {
    'siena': {'nums': [1,2,3]},
    'firenze': {'nums': [4,5,6]}
}


for k in my_dict:
    print(my_dict[k]['nums'])


my_dict_2 = {
    'siena': [1,2,3],
    'firenze': [4,5,6],
    'tutte': [9,9,9]
}


excluded_k = ['tutte']

new_d = {k: my_dict_2[k] for k in set(list(my_dict_2.keys())) - set(excluded_k)}

print(new_d)

d = {}

print(bool(d))