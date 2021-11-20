def my_sum(n):
    if n == 0:
        return 0
    else:
        return n + my_sum(n - 1)


def my_even_sum(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        n = n - 1
    else:
        return n + my_even_sum(n - 2)


def my_odd_sum(n):
    if n == -1:
        return 0
    elif n % 2 == 0:
        return my_odd_sum(n - 1)
    else:
        return n + my_odd_sum(n - 2)
