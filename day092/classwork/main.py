def replace_dots(s):
    return s.replace('.', '-')


def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient // new_exponent
    return f"{new_coefficient}x^{new_exponent}"


def is_kiss(words):
    return " " not in words


print(replace_dots("one.two.three"))  
print(integrate(3, 2))                 
print(is_kiss("codewars"))            
print(is_kiss("hello world"))       