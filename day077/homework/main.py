def even_sum(numbers):
    total = 0 
    for num in numbers: 
        if num % 2 == 0:  
            total += num  
    return total 
print(even_sum([1, 2, 3, 4, 5, 6])) 

def count_letter(text, letter):
    count = 0 
    for char in text: 
        if char == letter: 
            count += 1
    return count
print(count_letter("Hello World", "l"))


def common_elements(list1, list2):
    lst = [] 
    for x in list1: 
        if x in list2 and x not in lst:
            lst.append(x)
    return lst
print(common_elements([1, 2, 3], [2, 3, 4]))