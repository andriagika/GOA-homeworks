# # 2) კომენტარის სახით ჩამოწერეთ ყველა სტრინგის მეთოდი, რომელიც ისწავლეთ. თითოეულს მიუწერეთ დეტალური განმარტება და მათზე მოიყვანეთ თითო-თითო მაგალითი. 
# # # .upper() ასოებს ადდიდებს 
# # print("wORld".upper())
# # # .lower()ასოებს აპატარავებს
# # print("wORld".lower())
# # # .capitalize() ასოებს ასტაბილურებს
# # print("wORld".capitalize())
# # # 2) მომხმარებელს შემოატანინეთ სიტყვა. ტერმინალში კი დაბეჭდეთ ეს სიტყვა ისე რომ იყოს:
# # word = input("Enter your word: ")
# # print(f"all small word {word}".lower())
# # print(f"all big word {word}".upper())
# # print(f"first word big all small word {word}".capitalize())
# # # 1. ყველა პატარა ასო;
# # # 2. ყველა დიდი ასო;
# # # 3. პირველი ასო დიდი, ხოლო ყველა დანარჩენი პატარა.

# # # 3) მომხმარებელს შემოატანინეთ სამი წინადადება და თითოეულზე გამოიყენეთ სხვადასხვა სტრინგის მეთოდი:
# # # პირველ წინადადებაზე — .lower()
# # # მეორე წინადადებაზე — .upper()
# # # მესამე წინადადებაზე — .capitalize()
# # word1 = input("Enter your word: ")
# # word2 = input("Enter your word: ")
# # word3 = input("Enter your word: ")
# # print(f"all small word {word1}".lower())
# # print(f"all big word {word2}".upper())
# # print(f"first word big all small word {word3}".capitalize())
# # 4) ცვლადში შეინახე შენი სახელი. მომხმარებელს შეეკითხე თავისი სახელი, იმ შემთხვევაში თუ თქვენი სახელები ემთხვევა დაბეჭდეთ "Our names are similar!", თუ არ ემთხვევა დაბეჭდეთ "We have different names". გაითვალისწინეთ, რომ მომხმარებელმა შეიძლება თქვენნაირი სახელი შემოიტანოს, თუმცა სახელის ასოები შესაძლოა იყოს სხვადასხვა შრიფტის ზომით, ამიტომ ამან თქვენ პროგრამაში შეფერხება არ უნდა გამოიწვიოს (გამოიყენეთ ნასწავლი სტრინგის მეთოდები)
# # name = "Andria"
# # name1 = input("What is your name?: ")
# # if name.capitalize() == name1.capitalize():
# #     print("Our names are similar!")
# # else:
# #     print("We have different names")
 
# # 5) ცვლადში შეინახეთ წინადადება, დაწერეთ ისეთი პროგრამა რომ მხოლოდ წინადადების პირველი ასო იყოს დიდი ასოთი, დანარჩენი კი იყოს პატარა.
# ngl = "bmw f90"
# ngl2 = ngl.capitalize()
# # 6) ცვლადში შეინახეთ რაიმე სტრინგი, შემდეგ .find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო.
# text = "Megatron"
# index = text.find("r")
# print("word 'r' are at index:", index)
# # 7) შექმენით სია, სადაც დაამატებთ რანდენიმე სტრინგს. სიაში დამატებული თითოეული სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით.
# words = ["cat", "dog", "parrot", "tiger"]
# words1 = []
# for word in words:
#     words1.append(word.upper())
# print(words1)
# # 8) ჩანაწერს გადახედეთ თავიდან.