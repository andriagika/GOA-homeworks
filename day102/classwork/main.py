# 1) მოცემულია Dictionary:
# თქვენი დავალებაა შეცვალოთ 'Chemisty' key-ს მნიშვნელობა 'A'-ით.
student_grades ={
    'Math': 'A',
    'Biology': 'C',
    'Chemistry': 'B',
    'English': 'A',
}

student_grades['Chemistry'] = "A"
print(student_grades)


# 2) გამოიყენეთ update() მეთოდი, რომ წინა დავალების Dict-ში დაამატოთ ახალი key & value მნიშვნელობა 'Physics' : 'A'.
# შემდეგ კი ამოაგდეთ 'Biology' Dict-იდან.
student_grades.update({"Physics": "A"})
student_grades.pop("Biology")
print(student_grades)
# 3) შექმენით ნებისმიერი Dict (Min. 4 მნიშვნელობით). გამოიყენეთ List Comprehension, რომ სიაში შეინახოთ  ამ Dict-ის ყველა value.
car_prices = {
    "BMW": 30000,
    "AUDI": 28000,
    "MERCEDES": 35000,
    "TOYOTA": 20000,
}

values_list = [value for value in car_prices.values()]

print(values_list)