fruits = ('Apple', 'Pomegranate', 'Cherry', 'Strawberry', 'Blueberry')
*fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3)

numbers = [1, 2, 3, 4, 5]
*a, b, c = numbers
print(a, b, c)

letters = ('a','b','c','d','e')
x, *y, z = letters
print(x, y, z)

my_list = [1, 2, 3]
my_tuple2 = (4, 5, 6)
print("List:", my_list)
print("Tuple:", my_tuple2)

my_tuple = (10, 20, 30, 40, 50, 60, 70)
a, b, c, *d = my_tuple
print(a, b, c, d)
