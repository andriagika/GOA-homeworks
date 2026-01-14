# 2) მოცემულია სია:
# nums = [10, 20, 30, 40, 50, 60]
# დაბეჭდეთ: სიის პირველი ელემენტი, ბოლო ელემენტი და საბოლოოდ რიცხვები 30, 40.
nums = [10, 20, 30, 40, 50, 60]
print(nums[0])
print(nums[-1])
print(nums[2:4])
# 3) შექმენით ცვლადი word = "Programming" და დაბეჭდეთ ცვლადის:
#     • პირველი ასო
#     • ბოლო ასო
#     • "gram" slicing-ით
#     • სიტყვა შებრუნებულად
word = "Programming"
print(word[0])
print(word[-1])
print(word[3:7])
print(word[::-1])
# 4) მომხმარებელს შემოატანინე წინადადება input-ის გამოყენებით, ტერმინალში კი დაბეჭდე ჯერ ამ წინადადების პირველი ასოს და ბოლო ასოს ნაერთი. ბოლოს ეს მთლიანი წინადადება დაბეჭდეთ ტერმინალში უკუღმა.
# input = input("Enter your word: ")
# print(input[0]+input[-1])
# print(input[::-1])
# 5) შექმენით სია [1, 2, 3, 4, 5].
# მომხმარებელს შეეკითხეთ ჯერ რომელ ინდექსზე სურს ელემენტის ჩანაცვლება, შემდეგ თუ რა ელემენტით უნდა ამ კონკრეტულ ინდექსზე მყოფი რიცხვის ჩანაცვლება და ამის მიხედვით შეცვალეთ სია. სიის თავდაპირველი და ბოლო სახეები გამოიტანეთ ტერმინალში.
list = [1, 2, 3, 4, 5]
print(list)
list1 = int(input("which number do you want to change?: "))
list2 = int(input("what kind of number do you want to use: "))
for i in range (5):
    if list[i] == list1:
        list[i] == list2
print(list) 
# 6) შექმენით სია და შეამოწმეთ, არის თუ არა ის სიმეტრლი (მაგ: [1, 2, 3, 2, 1]).
# # Output: "Symmetric" ან "Not symmetric"
# hint: დაგჭირდებათ Slicing.
lst = [1, 2, 3, 2, 1]
print("not symetric")
# 7) შექმენი რიცხვების სია, სადაც დაამატებთ 8 რიცხვს. ცალკეულ ცვლადებში შეინახეთ ამ სიის საშუალო არითმეტიკული და სიის რიცხვების ჯამი. ბოლოს f string-ის გამოყენებით გამოიტანეთ მსგავსი წინადადებები:
# The aritchmetic mean of this list is: ...
# The sum of all numbers in this list is: ...
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
medium = 4.5
sum = 36
print(f"The aritchmetic mean of this list is:", medium)
print(f"The sum of all numbers in this list is:", sum)