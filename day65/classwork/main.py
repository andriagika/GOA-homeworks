def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def vowels_counter(text):
    vowels = "aeiou"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

print(vowels_counter("goa oriented"))

