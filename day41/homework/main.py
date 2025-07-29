# 2) მომხმარებელს შემოატანინეთ რამდენიმე სიტყვა და შეინახეთ ისინი სიაში.
# საბოლოოდ დაბეჭდეთ ამ სიის სიგრძე len() ფუნქციის გამოყენებით. 
word1 = input("Enter your 1 word: ")
word2 = input("Enter your 2 word: ")
word3 = input("Enter your 3 word: ")
word = []
word.append(word1)
word.append(word2)
word.append(word3)
print(f"The lenght of list are: ",{len(word)})
# 3) შექმენით ცარიელი სია. მომხმარებელს 3-ჯერ შემოატანინეთ რაიმე მონაცემი და ყოველ ჯერზე დაამატეთ ის სიაში append() ფუნქციით.
# ბოლოს დაბეჭდეთ სია.
# ცარიელი სიის შექმნა
list = []
for i in range(3):
    item = input(f"Enter your element #{i+1}: ")
    list.append(item)
print("inside of list are:", list)

# 4) შექმენით Fruits სია 4 ელემენტით.
# მომხმარებელს შემოატანინეთ ახალი ხილი და ჩასვით ის სიის მეორე ინდექსზე.
# საბოლოოდ ტერმინალში გამოიტანეთ განახლებული სია.
# Create a list with 4 fruits
fruits = ["apple", "banana", "peach", "pear"]
new_fruit = input("Enter a new fruit: ")
fruits.insert(2, new_fruit)
print("Updated fruit list:", fruits)

# 5) შექმენით სია [“car”, “bike”, “bus”, “train”, “plane”].
# ჯერ სიიდან ამოაგდეთ მეოთხე ინდექსზე მყოფი ელემენტი, შემდეგ კი ბოლო ელემენტი და გამოიტანეთ მთლიანი სია ეკრანზე.# Create the initial list
vehicles = ["car", "bike", "bus", "train", "plane"]
vehicles.pop(4)
vehicles.pop()
print("Updated list:", vehicles)
