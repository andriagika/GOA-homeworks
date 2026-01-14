# Lambda არის ფუნქცია რომელსაც ვიყენებთ მაშინ როცა ფუნქცია ერთჯერადად გვჭირდება.
# map - შეგვიძლია iterable-ის ელემენტები შევცვალოთ ან მის თითოეულ ელემენტს მივწვეთ.
# filter - შეგვიძლია კონკრეტული პირობის მიხედვით გავფილტროთ ელემენტები

celsius = [0, 25, 100, -10, 37]
kelvin = list(map(lambda c: c + 273, celsius))
print(kelvin)

numbers = [2, 4, 6, 8, 10]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

usernames = []
for i in range(5):
    name = input("Enter username: ")
    usernames.append(name)
greet_users = list(map(lambda name: "Welcome " + name, usernames))
print(greet_users)

cars = {
    "BMW E36": 1998,
    "Mercedes W210": 2001,
    "Audi A4": 1999,
    "Toyota Corolla": 2005,
    "Honda Civic": 1997
}
old_years = list(filter(lambda car: car[1] < 2000, cars.items()))
print(old_years)

usernames = []
for i in range(5):
    name = input("Enter username: ")
    usernames.append(name)
filtered_users = list(filter(lambda name: len(name) > 5, usernames))
print(filtered_users)
