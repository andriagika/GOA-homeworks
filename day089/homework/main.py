def get_vowel_count(s):
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

def sum_digits(number):
    return sum(int(d) for d in str(abs(number)))

def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())

print(get_vowel_count("codewars"))    
print(sum_digits(-31415))             
print(to_jaden_case("hello world"))     