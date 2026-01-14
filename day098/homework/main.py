t1 = (1, 2, 3)
a, b, c = t1
print(a, b, c)

t2 = ('apple', 'banana', 'cherry')
x, y, z = t2
print(x, y, z)

t3 = (10, 20)
p, q = t3
print(p, q)

info = ('John', 25, 'Tbilisi', 'Developer', 'Blue')
name, age, city, job, fav_color = info
print(name, age, city, job, fav_color)


numbers = (5, 10, 15, 20, 25)
num1, *rest = numbers
print(num1, rest)
