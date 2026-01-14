numbers = {1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 2}
print(numbers)

languages = {'HTML', 'CSS', 'JavaScript', 'Python'}
languages.remove('JavaScript')
languages.add('React')
print(languages)

countries = {'Georgia', 'USA', 'France'}
countries.clear()
countries.add('Tbilisi')
countries.add('New York')
countries.add('Paris')
print(countries)

set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
combo = set1.union(set2)
print(combo)

fruits = {'apple', 'banana'}
fruits.add('cherry')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.discard('orange')
print(fruits)

removed = fruits.pop()
print(removed)
print(fruits)

my_info = {
    'name': 'John',
    'surname': 'Doe',
    'age': 25,
    'height': 180,
    'fav_color': 'Blue',
    'fav_cars': ['BMW', 'Audi', 'Tesla']
}

print(my_info.get('name'))
print(my_info.get('surname'))
print(my_info.get('age'))
print(my_info.get('height'))
print(my_info.get('fav_color'))
print(my_info.get('fav_cars'))

fav_car = {
    'name': 'Model S',
    'brand': 'Tesla',
    'color': 'Red',
    'year': 2022,
    'engine': 'Electric',
    'horse_power': 670
}

for key, value in fav_car.items():
    print(key, ":", value)

my_dict = {
    'city': 'Tbilisi',
    'country': 'Georgia',
    'population': 1200000,
    'river': 'Kura',
    'famous_place': 'Narikala'
}

for key in my_dict:
    my_dict[key] = str(my_dict[key]) + "_updated"

print(my_dict)
