def read_numbers():
    a, b = map(int, input("введите 2 числа через запятую\n").split(" "))
    return a, b


def read_operation():
    operator = input("введите арифметический оператор из предложенных: +, -, *, /, ^\n")
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


def calculator():
    a, b = read_numbers()
    operator = read_operation()
    if operator == "+":
        print(calc_sum(a, b))
    elif operator == "-":
        print(calc_diff(a, b))
    elif operator == "*":
        print(calc_mul(a, b))
    elif operator == "/":
        print(calc_div(a, b))
    elif operator == "^":
        print(calc_pow(a, b))
    else:
        print("неверрный ввод")


calculator()
