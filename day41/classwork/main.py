# # 1) კომენტარის სახით ახსენით რას აკეთებს len(), append(), insert() და pop() ფუნქციები
# len() გვეუბნევა თუ რამდენი ინდექსია ან სიმბოლო სიაში
# append() ამატებს ინდექს სიის ბოლოს
# insert() ამატებს ინდექს ორ ინდექს შორის
# pop() აგდებს ინდექს სიიდან
# 2) შექმენით სია და შეინახეთ  5 სახელი. მომხმარებელს შემოატანინეთ სახელი და დაამატეთ ამ სიაში. ბოლოს, დაბეჭდეთ ამ სიის სიგრძე და სიის განახლებული ვერსია.
list = ["Andria", "Luka", "Leqso", "Nika", "Gio"]
list1 = input("Enter your name: ")
list1 = list.append(list1)
print(len(list))
print(list)
# 3) შექმენით სია: fruits = ["Melon", "Orange", "Cantaloupe", "Watermelon", "Kiwi"]
# ამოაგდეთ სიიდან ბოლო ელემენტი და მესამე ინდექსზე ჩასვით "Pomegranate".
fruits = ["Melon", "Orange", "Cantaloupe", "Watermelon", "Kiwi"]
fruits.pop(4)
fruits.insert(3, "Pomegranate")
print(fruits)