
def hello(name=""):
    if not name:
        return "Hello, World!"
    return f"Hello, {name.capitalize()}!"


def sum_mix(arr):
    return sum(int(x) for x in arr)

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        raise ValueError("Invalid operator")


def litres(time):
    return time // 2

def century(year):
    return (year + 99) // 100