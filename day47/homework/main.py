def manual_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(manual_sum([1, 2, 3, 4, 5]))

def user_info(name, surname, age):
    return f"{name} {surname} is {age} old."
print(user_info("Andria", "Gikashvili", 14))


def Arithmetic_mean(numbers):
    if len(numbers) == 0:
        return 0 
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
print(Arithmetic_mean([10, 20, 30]))

def filter_vowels(text):
    vowels = "abcdefghi"
    result = ""
    for char in text:
        if char in vowels:
            result += char
    return result
print(filter_vowels("hello, how are you?"))
