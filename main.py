def read_numbers():
    a, b = map(int, input("введите 2 числа через запятую").split(" "))
    return a, b


def read_operation():
    operator = input()
    return operator


def calc_sum(a, b):
    return a + b


def calc_diff(a, b):
    return a - b


def calc_mul(a, b):
    return a * b


def calc_div(a, b):
    return a / b


def calc_pow(a, b):
    return a ** b
