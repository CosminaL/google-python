import copy

print('Hello World!')
""" This is out first Python course
we learn about different data structures
"""
# acesta e un comentariu

first_number = 7
second_number = 8
print(first_number is not second_number)  # daca obectul are aceeasi adresa de memorie

# dictionar
source = dict()  # dictionar
copy1 = source  # copia va pointa spre aceeasi adresa de memorie a source
print(source is copy1)

# operatori de apartenenta
print(1 in [1, 3, 2])
print('y' not in 'Python')

print("si Dumnezeu a zis: 'Sa se faca lumina!'")

print(r"Somnoroase pasarile\nPe la cuiburi se aduna.")  # raw string - exact asa cum este
print(""" poti sa scri ce doresti 

ce doresti
   si cum doresti""")  # pastreaza exact asa cum am scris

# placeholders
output_str = "for only price {price:2.2f} dollars {cheers_msg}".format(price=49, cheers_msg="Have a great day!")
print(output_str)

# List
l = ['A', 'n', 'a']
print(l)
l[0] = 'a'  # lists are mutable
print(l)

new_l = [1, '2', 'Ana are mere', [9, 10, 11], None]
print(new_l)
print(new_l[-1])  # first element
print(new_l[3:])  # 3 inclusive
print(new_l[:3])  # 3 exclusive
print(new_l[1:3])  # both inclusive
print(new_l[1::2])  # de la 1 din 2 in 2
print(new_l.index(1))  # where el 1 is found

# second_list = list(l)
second_list = l[::]  # make a copy of of the list
print(second_list)

print(second_list.sort())
print(sorted(second_list))

source = {
    1: "Ana",
    2: "are",
    3: "mere",
    4: {
        'a': 'a',
        'b': 'b',
        'c': 'c'
    }
}

print(source[2])
print(source.get(2))  # value of key 2 -> NOT: source[2] => NULL
print(source.get(5, "Invalid key!"))
print(source.keys())  # dict_keys
print(source.items())  # dict_items
print(source.values())  # dict_values
for key, value in source.items(): # or kwargs.values() -> takes only values
    print(f'{key} -> {value} ')  # inlocuirea directa a placeholders

# copy dictionaries
first_copy = source
second_copy = source.copy()
third_copy = copy.deepcopy(source)
source[1] = 00000  # second_copy doesn't change
print(source)
print("first copy: ", first_copy)
print("second copy: ", second_copy)

source[4]['a'] = '00000'  # second_copy is also changed -> copy() makes a shallow copy (only on the 1st lvl)

print("second copy: ", second_copy)
print("third copy: ", third_copy)

l = {1, 2, 1, 3, 4, 3, 4, 2, 2}
# get list of unique elements
s = set(l)  # eliminate duplicates
print(list(s))  # list of unique elements
