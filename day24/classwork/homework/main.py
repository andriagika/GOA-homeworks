# 2) დაწერეთ პროგრამა, სადაც თავდაპირველად მომხმარებელს შემოატანინებთ ანგარიშის პაროლს, შემდეგ შეეკითხეთ რომ გაიმეოროს იქამდე, სანამ არ დაემთხვევა შეყვანილი პაროლი.

# pas = input("enter your password: ")

# pas2 = input("repeat your password: ")

# while pas != pas2:
#     pas2 = input("repeat your password: ")

# if pas == pas2:
#     print("finish")

# 3) შექმენით Number guess game:

# ცვლადში შეინახეთ სასურველი რიცხვი. მომხმარებელს Input-ის მეშვეობით შეეკითხეთ ეცადოს რიცხვის გამოცნობა, ვერ გამოცნობის შემთხვევა გამოუტანეთ "Try again" და იქამდე გამოუტანეთ Input ველი სანამ არ გამოიცნობს რიცხვს. წარმატებით გამოცნობის შემთხვევაში გამოუტანეთ "You guessed the number sucessfully!".

# num = 10

# num2 = int(input("Guess a number: "))

# while num != num2:
#     num2 = int(input("Try again: "))

# if num == num2:
#     print("You guessed the number sucessfully!")

# 4) შექმენით სია, სადაც შეინახავთ თქვენს საყვარელ ცხოველებს. გამოიტანეთ სიიდან პირველი და ბოლო ელემენტი და ერთ ხაზზე დაბეჭდეთ.

# animals = ["rino", "lion", "tiger"]
# print(animals[0], animals[2])

# 5) შექმენით სია და მასში შეინახეთ თქვენი საყვარელი ფერები (მინიმუმ 5). გამოიყენეთ უარყოფითი ინდექსინგი (Negative Indexing) იმისთვის, რომ გამოიტანოთ სიის მესამე ელემენტი.

# colors = ["red", "blue", "yellow", "green", "orange"]
# print(colors[-3])

# ----------
# HARD LEVEL:

# შექმენით სახელების სია და მასში დაამატეთ 3 სახელი, თუმცა სამივე სახელი უნდა იყოს მომხმარებლის მიერ შემოტანილი. დაბეჭდეთ სიის მნიშვნელობა.


# name_list = []

# for i in range(3):
#     name = input(f"enter your names #{i+1}: ")
#     name_list.append(name)

# print("entered names are:", name_list)
