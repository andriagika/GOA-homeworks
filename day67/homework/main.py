
def reverse_lst(lst):
    return lst[::-1]

def reverse_str(s):
    return s[::-1]

def double(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num * 2)
    return new_lst


def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def max_num(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum



def min_num(lst):
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum
