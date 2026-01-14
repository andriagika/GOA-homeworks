# 1-სინტაქსური ერორი მაგ:არასწორი ინდენტაცია
# 2- ლოგიკური ერორი მაგ:არასწორი ინდეხსი
# SyntaxError,TypeError,NameError,ValueError


numbers= [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Such index doesn’t exist")

