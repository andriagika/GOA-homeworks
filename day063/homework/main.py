def distinct(arr):
    result = []
    seen = set()
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    return your_points > average


def kata_13_december(lst):
    return [x for x in lst if x % 2 != 0]


def people_with_age_drink(age):
    if age < 14:
        return "Kids drink toddy."
    elif age < 18:
        return "Teens drink coke."
    elif age < 21:
        return "Young adults drink beer."
    else:
        return "Adults drink whisky."
    
def repeat_str(repeat, string):
    return string * repeat