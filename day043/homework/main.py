# ფუნქციებს ვიყენებთ იმიტომ, რომ: კოდი გავიმარტივოთ დa ფუნქციის დაწერის შემდეგ მას მრავალჯერ გამოვიყენებთ სხვადასხვა მონაცემზე, კოდის გადაწერის გარეშე.დავზოგოთ დრო და რესურსები

def user_info(name, age):
    return f"{name} is {age} years old"
print(user_info("Andria", 14))

def square(number):
    return number ** 2
print(square(6)) 

def power(a, b):
    return a ** b
print(power(2, 5))

def double_values(numbers):
    return [x * 2 for x in numbers]
print(double_values([1, 2, 3]))

def square_list(numbers):
    return [x ** 2 for x in numbers]
print(square_list([2, 3, 4]))

def sum(a, b, c):
    return a + b + c
print(sum(5, 10, 15)) 

def substract(a, b):
    return a - b
print(substract(10, 3))

def multiply(a, b):
    return a * b
print(multiply(4, 6))

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0 cannot be divided"
print(divide(10, 2))
print(divide(10, 0))





