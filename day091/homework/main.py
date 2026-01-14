def odd_index(arr):
    for i, v in enumerate(arr):
        if v == i:
            return v
    return None

def dont_give_me_five(start, end):
    count = 0
    for n in range(start, end + 1):
        if '5' not in str(n):
            count += 1
    return count

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump
