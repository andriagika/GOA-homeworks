# 2) კომენტარის სახით ახსენით რატომ ვიყენებთ Slicing-ს Python-ში.
# slicing-ს პითონში იმიტომ ვიყენებთ რომ კონკრეტული ნაწილი გამოვიტანოთ სიის ან სტრინგის და არა მთლიან ნაწილი.

# 3) შექმენით რიცხვების სია, სადაც შენახული გექნებათ 10 რიცხვი. Slicing-ის მეშვეობით გამოიტანეთ ამ სიის პირველი ხუთი რიცხვი და გამოიტანეთ ტერმინალში.
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(numbers[:5])
# 4) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Academy".
word = "Goal-Oriented Academy"
print(word[14:])

# 5) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Oriented".
word1 = "Goal-Oriented Academy"
print(word1[5:13])
# 6) ცვლადში შეინახეთ თქვენი გვარი. ინდექსინგის საშუალებით გამოიტანეთ თქვენი გვარის პირველი, ბოლო და შუა ასოები.
surname = "Gikashvili"
print(surname[0])
print(surname[-1])
print(surname[1:9])
# 7) შექმენით სია colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
# სიიდან გამოიტანეთ მხოლოდ Black და Yellow.
colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
print(colors[:2])

# 8) შეინახეთ ცვლადში "Hello, World!". Slicing-ის საშუალებით ამ სტრინგიდან  ამოიღეთ ცალკე სიტყვა "Hello" და ცალკე სიტყვა "World!". შეინახეთ ისინი ცვლადებში და გამოიტანეთ ეკრანზე.
word2 = "Hello, World!"

box1 = word2[0:5]
box2 = word2[7:]
print(box1)
print(box2)