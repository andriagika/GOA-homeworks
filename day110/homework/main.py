user_info = lambda name, surname, age: f"Name: {name}, Surname: {surname}, Age: {age}"
print(user_info("Giorgi", "Beridze", 20))

average = lambda numbers: sum(numbers) / len(numbers)
nums = [10, 20, 30, 40]
print(average(nums))

is_palindrome = lambda text: text == text[::-1]
print(is_palindrome("level"))  
print(is_palindrome("python")) 

check_number = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check_number(10))
print(check_number(-5))
print(check_number(0))

multiply_by_two = lambda numbers: list(map(lambda x: x * 2, numbers))
nums = [1, 2, 3, 4]
print(multiply_by_two(nums))

filter_strings = lambda words: [word for word in words if len(word) > 5]
strings = ["python", "js", "coding", "html", "programming"]
print(filter_strings(strings))

negative_numbers = lambda numbers: [num for num in numbers if num < 0]
nums = [5, -3, 10, -8, 0, -1]
print(negative_numbers(nums))
