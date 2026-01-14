def get_negatives(numbers):
    negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
    return negatives

print(get_negatives([5, -3, 0, -10, 8])) 


def get_positives(numbers):
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives

print(get_positives([5, -3, 0, -10, 8]))

def power_and_multiply(a, b, c):
    result = (a ** b) * c
    return result

print(power_and_multiply(2, 3, 4))
