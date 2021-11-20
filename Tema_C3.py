from my_package.recursive_module import *

# 1)

# def my_function(*args, **kwargs):
#     sum = 0
#     for var in args:
#         if isinstance(var, (float, int, complex)):
#             sum += var
#
#     print(sum)
#     # print(sum(args))
#
#
# my_function(1, 5, -3, 'abc', [12, 56, 'cad'])
# my_function()
# my_function(2, 4, 'abc', param_1=2)

# 2)

# def int_check():
#     my_var = input("Enter a value: ")
#
#     try:
#         my_int = int(my_var)
#     except ValueError as e:
#         print(0)
#     else:
#         print(f'The entered value is: {my_int}')
#
#
# int_check()

# 3)
if __name__ == '__main__':
    first_sum = my_sum(10)
    even_sum = my_even_sum(10)
    odd_sum = my_odd_sum(10)
    print(f"[0, n] sum: {first_sum}")
    print(f"even [0, n] sum: {even_sum}")
    print(f"odd [0, n] sum: {odd_sum}")







