def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def check_symbol_in_string(string, symbol):
    if symbol in string:
        return "Found"
    else:
        return "Not found"

def reverse_string(s):
    return s[::-1]

def unique_elements(lst):
    return list(set(lst))

def check_element(lst, element):
    if element in lst:
        return len(element)
    else:
        return len(lst)