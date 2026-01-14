user = {
    'username': 'John',
    'pass': 'J123',
    'creation year': 2016,
    'creation month': 10,
    'creation day': 28
}

user.update({'pass': 'J1997', 'creation day': 26})

for key, value in user.items():
    print(f"{key}: {value}")

print("-"*40)

product_amount = {
    'Bag': 13,
    'Heels': 5,
    'Jeans': 29,
    'Sweatshirt': 14,
    'Sunglasses': 30
}

product_amount.update({'Hat': 7})

print(product_amount)

print("-"*40)


product_amount['Sweatshirt'] = product_amount['Sweatshirt'] / 2
print("Half of Sweatshirt:", product_amount['Sweatshirt'])

print("-"*40)


my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Tbilisi',
    'job': 'Developer',
    'hobby': 'Reading'
}

keys_list = [key for key in my_dict]
print("Keys list:", keys_list)

print("-"*40)

languages = ['Python', 'Java', 'C', 'C++', 'JavaScript', 'Go', 'Rust', 'Ruby', 'Kotlin']
no_a_languages = [lang for lang in languages if 'a' not in lang]
print("Languages without 'a':", no_a_languages)

print("-"*40)

car_brands = ['Audi', 'BMW', 'Tesla', 'Honda', 'Ford', 'Mazda', 'Kia', 'Volvo']
short_brands = [brand for brand in car_brands if len(brand) <= 5]
print("Short brand names:", short_brands)
