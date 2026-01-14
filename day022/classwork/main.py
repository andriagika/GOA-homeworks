# 1) დაწერეთ თუ რა დანიშნულება აქვს if, elif და else-ს.

# 2) ცვლადში შეინახეთ თქვენი გვარი. შემდეგ მომხმარებელს შემოატანინეთ თავისი გვარი. თუ თქვენი გვარები დაემთხვევა გამოიტანეთ "Our surnames are similar", სხვა შემთხვევაში "Our surnames are not similar"

# 3) ცვლადში შეინახეთ თქვენი სიმაღლე. მომხმარებელსაც შეეკითხეთ მისი სიმაღლე.

# • თუ შენ უფრო მაღალი ხარ გამოიტანე: "I'm taller than you."

# • თუ მომხმარებელი უფრო მაღალია გამოიტანე: "You're taller than me"

# • თუ ტოლი სიმაღლეების ხართ, მაშინ დაბეჭდეთ "We have equal heights".

# if თან ვწერთ პირობას და დასაწყიში ვიყენებთ
# elif თანაც ვწერთ პირობას მაგრამ if ის მერე ვწერთ
# else არ უნდა პირობა და elif ან if მერე იწერება

surname1 = "Andria"
surname2 = input("enter your surname: ")

if surname1 == surname2:
    print("we have same surname")
else: 
    print("we dont have same surname")

high1 = 165
high2 = int(input("enter yoour height"))
if high1 == high2:
    print("we are same height")
elif high1 < high2:
    print("you are taller ")
else:
    print("you are shorter")