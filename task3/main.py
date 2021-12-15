def calculate(x, y, a, b):
    answer = (((x + (1 / y))) ** a) * ((x - (1 / y)) ** b) / \
        (((y + (1 / x)) ** a) * ((y - (1 / x)) ** b))
    return answer


print(calculate(2, 2, 1, 1))
