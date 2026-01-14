# 2) მოიყვანეთ მაგალითები და ახსენით თუ რატომ არის სტრინგი - Immutable და სია - Mutable.
# ამასთანავე ახსენით ტუ რას ეწოდება Mutable და Immutable.
# mutable : ეწოდება ისეთ ცვლადს რომლის შეცვლაც შემდეგშიც შეგვიძლია. 
# fruits = ["apple", "mango", "banana"]
# print(fruits)
# fruits[1] = "grape" 
# print(fruits)

# imutable : ეწოდება ისეთ ცვლადს რომელიც შექმნის მერე აღარ შეგვიძლია მისი შექმნა მაგ: სტრინგი
# brand = "BMW" 
# brand[0] = "A"


# 3) მომხმარებელს შემოატანინეთ თავისი სახელი, გვარი, ID ნომერი და ეროვნება. ეს ყოველივე შეინახეთ User_info ცვლადში.
#  ჯერ მთლიანი სია დაბეჭდეთ, შემდეგ კი ინდექსინგის საშუალებით გამოიტანეთ სიის თითოეული ელემენტი ტერმინალში.

# info = ["name", "surname", "id", "region"]
# info[0] = input("Enter your name: ")
# info[1] = input("Enter your surname: ")
# info[2]= int(input("Enter your id: "))
# info[3] = input("Enter your region: ")
# print(info)
# print(info[0])
# print(info[1])
# print(info[2])
# print(info[3])
# 4) შექმენით Vending Machine პროგრამა.

# შექმენით Vending Machine სია სადაც მინიმუმ 10 ცალ პროდუქტს დაამატებთ. მომხმარებელი უნდა ირჩევდეს პროდუქტის ინდექსს და შემდეგ თქვენ პროდუქტის დასახელება უნდა გამოუტანოთ ტერმინალში. (პირობაში დეტალები არ მიწერია, ასერომ ეცადეთ რაც შეიძლება დახვეწილი და მომხმარებლისთვის მოსახერხებელი პროგრამა შექმნათ)
# Vending_Machine = ["Snikers", "Twix", "Fanta", "Lay,s", "Oreo", "Drew", "Pepsi", "Doritos", "Bounty", "Gummy bears"]
# number = int(input("choose the product: "))
# for i in range(10):
#     if i == number:
#         print(Vending_Machine[i])

# 5) შექმენით Fruits სია: 
# Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
# სიის მეოთხე ელემეტი ჩაანაცვლეთ "Watermelon"-ით, მეორე ელემენტი კი "Pear"-ით. ტერმინალში დაბეჭდეთ სიის თავდაპირველი და საბოლოო სახე.
# Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
# print(Fruits)

# Fruits[-1] = "Watermelon"
# Fruits[1] = "Pear"
# print(Fruits)

# 6) რამდენიმე ცვლადში შინახეთ სხვადასხვა სიტყვა. ამ სიტყვების გამოყენებით ააწყვეთ ერთი მთლიანი სიტყვა. მაგ.
# ("Moon", "light" -- "Moonlight")
# puzzle = ["melon", "water", "sand"]
# print(puzzle[1] + puzzle[0])

# puzzle1 = ["witch", "jungle", "sand"]
# print(puzzle1[-1] + puzzle1[0])