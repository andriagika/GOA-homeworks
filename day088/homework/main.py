def get_count(sentence):
    vowel_count = 0
    vowels = "aeiou"
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def sumDigits(number):
    number = abs(number)
    return_number = 0
    
    while number > 0:
        return_number += number % 10
        number = int(number / 10)
        
    return return_number

def find_longest(arr):
    max_lenght = 0
    max_index = 0
    for cur_num in arr:
        lenght = len(str(cur_num))
        if lenght > max_lenght:
            max_lenght = lenght
            max_index = arr.index(cur_num)
    return arr[max_index]