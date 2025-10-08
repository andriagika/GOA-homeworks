def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def area_or_perimeter(l , w):
    if l == w:
        return l * w 
    else:
        return 2 * (l + w) 