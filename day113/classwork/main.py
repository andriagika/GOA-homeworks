# items = [
    # ('product1', 11),
    # ('product2', 9),
    # ('product3', 5),
# ]


# filtered = list(filter(lambda item: item[1] <= 10, items))

# min_item = (filtered[0])[1]

# for i in filtered:
    # min_item = i[1]

# food = ['Salad H', 'Burger J', 'Fries J', 'Watermelon H', 'Shawarma J', 'Carrot H', 'Apple H']

# prices = list(filter(lambda item: item[1], items))



languages = ["Python", "Java", "JavaScript", "C", "C++", "PHP", "Go", "Rust", "Ruby", "Kotlin"]
filtered = list(filter(lambda item: len(item) > 5, languages))
print(filtered)


# foods = [("salad ,H"), ("burger, J") , ("fish ,H"),("fries, J"),("fruits, H"),("nuts, H")]
# filtered1 = list(filter(lambda food: food[1] == , foods))
# print(filtered1) 

languages = ["Python", "Java", "JavaScript", "C", "C++", "PHP", "Go", "Rust", "Ruby", "Kotlin"] 
filtered2 = list(map(lambda lang: "I study " + lang, languages))
print(filtered2)

# minutes = [60, 120, 180, 240, 30]
# Hint: hours = minutes / 60