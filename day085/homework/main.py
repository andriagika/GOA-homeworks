def descending_order(num):
    num_str = str(num)
    digits = []
    for d in num_str:
        digits.append(d)
    digits.sort(reverse=True)
    new_num_str = ""
    for d in digits:
        new_num_str += d
    result = int(new_num_str)
    return result



def merge_arrays(arr1, arr2):
    combined = arr1 + arr2
    unique_numbers = list(set(combined))
    unique_numbers.sort()
    return unique_numbers


def divisible_by(numbers, divisor):
    result = []
    for n in numbers:
        if n % divisor == 0:
            result.append(n)
    return result

def between(a, b):
    result = []
    for i in range(a, b + 1):
        result.append(i)
    return result

def switch_it_up(number):
    if number == 0:
        return "Zero"
    elif number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"






