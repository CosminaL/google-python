import random
from my_package.my_module import my_var as tagged_var, my_func
from my_package.my_second_module import my_second_Var

# print('Curs 3\n\n')
#
# for i in range(10):
#     print(f'Set instructiuni [{i + 1}]')
#
# l = [i for i in range(1, 11) if i % 3 == 0]
#
# while True:
#     random_choice = random.choice([i for i in range(11)])  # list comprehension
#     if random_choice % 3 == 0:
#         break;
#
# print(f'random choice is: {random_choice}')
#
# for i in range(10):
#     if i % 2 != 0:
#         continue;
#     print(f'Numar par: {i}')
#
#
# # FUNCTIONS
#
# def get_sum(a, b):
#     return a + b
#
#
# my_sum = get_sum(1, 2)
# print(my_sum)
#
#
# # positional parameters
# def my_function(param_1, param_2):
#     print('param_1', param_1)
#     print('param_2', param_2)
#
#
# my_function(1, 2)
#
#
# # key=value -> required
# def my_function_2(param_1, param_2, param_3=3, param_4=4):
#     print('param_1', param_1)
#     print('param_2', param_2)
#     print('param_3', param_3)
#     print('param_4', param_4)
#
#
# my_function_2(1, 2, param_3=5)
#
#
# # undefined parameters
# def my_function_3(nume, prenume, **kwargs):
#     print('param_1', nume)
#     print('param_2', prenume)
#     # print(args)# print the rest of parameters
#     print(kwargs)  # key arguments - as a dictionary
#     for key, vars in kwargs.items():
#         print(f'{key}: {vars}')
#
#
# my_function_3('Popescu', 'Ion', telefon=745789277, mail='popescu.ion@gmail.com')  # phone no doesn't start with 0
#
# # Exceptions
#
# my_var = input("introduceti un nr: ")  # enter in console
# try:
#     my_int = int(my_var)
# except ValueError as e:
#     print("Please enter a number!")
# else:
#     print("Thank you for the entered value!")
#     # if no exception
#
#
# # Namespaces
#
# def my_function():
#     def my_second_function():
#         print(f'{msg}')
#
#     msg = "Hello world!"
#
#     my_second_function()
#
#     print(f"my_function: {msg}")
#
# my_function()

if __name__ == '__main__': # pt ca in  python nu exista main
    print(tagged_var)
    print(my_func())
    print(my_second_Var)

#pb 2 : Exceptions


