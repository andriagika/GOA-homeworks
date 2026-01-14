# 1-სინტაქსური ერორი მაგ:არასწორი ინდენტაცია
# 2- ლოგიკური ერორი მაგ:არასწორი ინდეხსი
# SyntaxError,TypeError,NameError,ValueError

x = 10 / 0  # ZeroDivisionError
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Can’t divide a number by 0.")

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    a = float(a)
    b = float(b)
    result = a / b
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

user_data = {
    "name": "John",
    "age": 25,
    "email": "john@example.com"
}
try:
    print(user_data["address"])
except KeyError:
    print("This key does not exist in the dictionary.")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Please Enter numbers only.")

