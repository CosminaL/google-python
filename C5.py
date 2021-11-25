print('Cursul 5')
print('-' * 50)

# LAMBDA
my_lambda = lambda x, y: x + y  # anonymous function

print('suma = ', my_lambda(2, 3))
# OR
print((lambda x, y: x + y)(9, 1))

players = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'rank': 3
    },
    {
        'first_name': 'Kevin',
        'last_name': 'McDonald',
        'rank': 1
    },
    {
        'first_name': 'Brad',
        'last_name': 'Kelvin',
        'rank': 1
    }
]

print(players)
sorted_players = sorted(players, key=lambda player: player['rank'])
print(sorted_players)


# MAP
def check_top_3_player(player):
    updated_player = player.copy()
    updated_player['is_top_3'] = True if player['rank'] <= 3 else False

    return updated_player


# Print_1
top_player = list(map(check_top_3_player, players))  # results a map type iterable
print(top_player)

# Print_2
for player in map(check_top_3_player, players):
    print(player)

# ZIP
letters = ['a', 'b', 'c', 'z']
numbers = [1, 2, 3, 4]

for l, n in zip(letters, numbers):
    print(l, ': ', n)

# LIST COMPREHENSION
my_numbers = [1, 2, 3, 4, 5]
squared_numbers = [item ** 2 for item in my_numbers]
print(squared_numbers)

squared_even_numbers = [item ** 2 for item in my_numbers if not item % 2]
print(squared_even_numbers)

# FILES

import csv

with open('data.csv', 'r') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for row in rows:
        print(row)



