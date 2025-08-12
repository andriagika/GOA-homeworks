def filter_positives(numbers):
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives
print(filter_positives([-5, 0, 3, 7, -2, 10]))

def filter_negatives(numbers):
    negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
    return negatives
print(filter_negatives([-5, 0, 3, 7, -2, 10]))

def name_to_upper(name):
    return name.upper()
print(name_to_upper("Andria"))
print(name_to_upper("Luka"))  
