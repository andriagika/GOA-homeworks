def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")

check_age(20) 
check_age(15)  

def print_names(names):
    for name in names:
        print(name)

print_names(["ANDRIA", "LUKA", "LEKSO"])

def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_or_even(4))
print(odd_or_even(7))  


def student_grade(score):
    if 90 <= score <= 100:
        print("A")
    elif 70 <= score <= 89:
        print("B")
    elif 50 <= score <= 69:
        print("C")
    elif 0 <= score <= 49:
        print("F")
    else:
        print("Invalid score")

student_grade(95)
student_grade(73) 
student_grade(60)
student_grade(30)
student_grade(110)
