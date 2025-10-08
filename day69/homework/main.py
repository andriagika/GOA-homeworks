def count_number(lst, choice):
    count = 0
    for num in lst:
        if num == choice:
            count += 1
    return count


def clear_list(lst, answer):
    if answer.lower() == "კი":
        lst.clear()
        print("სია გასუფთავდა:", lst)
    else:
        print("სია დარჩა:", lst)

fruits = ["apple", "banana", "orange", "kiwi", "mango"]

index = 2 
if 0 <= index < len(fruits):
    fruits.pop(index)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
