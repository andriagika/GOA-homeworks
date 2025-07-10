# # 3
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# num4 = int(input("Enter the forth number: "))
# num5 = int(input("Enter the fifth number: "))

# numbers = [num1, num2, num3, num4, num5]
# total = sum(numbers)
# mean = total / len(numbers)

# print(f"The arithmetic mean of this list is: {mean} ")
# print(f"The sum of all numbers in this list is: {total} ")

# # 4
# words = ["", "", "", "", ""]

# i = 0
# while i < 5:
#     word = input("Enter a word: ")
#     words[i] = word
#     i += 1
# for word in words:
#     print(word)

# # 5
# number = int(input("Enter number: "))
# if number % 2 == 0:
#     print("The number is even")
# # else:
#     print("The number is odd")

# 6
days = ["", "", "", "", "", "", ""]
i = 0
while i < 7:
    day = input("Enter a week days: ")
    days[i] = day
    i += 1
print("\even week days:")
for index in range(1, len(days)):
    if index % 2 == 0:
        print(days[index])