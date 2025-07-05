# 1) მომხმარებელს შემოატანინეთ 5 რიცხვი, რომლებსაც შემდეგ სიაში შენახავთ. Indexing-ს გამოყენებით გამოიტანეთ სიის ორი შუა ელენეტი.
box = [1, 2, 3, 4, 5]
print(box[1:3])
print(box[2:4])
# 2) მოცემული გაქვთ ცვლადი 
# alphabet ="abcdefghijklmnopqrstuvwxyz"
# Slicing-ის საშუალებით გამოიტანეთ ჯერ სტრინგის პირველი ხუთი სიმბოლო, შემდეგ ბოლო 5 სიმბოლო. ბოლოს ორივე ცალ-ცალკე შემოაბრუნეთ, შეაერთეთ და დაბეჭდეთ.
alphabet ="abcdefghijklmnopqrstuvwxyz"
word = alphabet[:5]
word1 = alphabet[-5:]
print(word[::-1] + word1[::-1] )
# 3) მოცემულია სტრინგი: text = "IndexingAndSlicingIsPowerful"
#  ამოიღეთ text ცვლადიდან სიტყვა "Indexing". შემდეგ შეაბრუნეთ და გამ მნიშვნელობის ყოველი მესამე ელემენტი ამოიტანეთ შედეგის სახით ეკრანზე.
text = "IndexingAndSlicingIsPowerful"
print(text[:8])
print(text[::-3])

# 4) მომხმარებელს შემოატანინეთ რამოდენიმე ჯანსაღი საკვები, შეინახეთ ცვლადში. შეაბრუნეთ და ბოლო 3 ელემენტი გამოიტანეთ ეკრანზე უარყოფითი Indexing-ის საშუალებით

healthy = ["salad", "egg", "tomato", "potato", "cucumber", "eggplant"]
print(healthy[2::-1])