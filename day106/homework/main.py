# // დანიშნულება finally, else და raise keyword-ების

# // finally : ყოველთვის მუშაობს, მიუხედავად იმისა, კოდში გაიპარა შეცდომა თუ არა.
# // else : შესრულდება მხოლოდ მაშინ, თუ try-ს ხაზში  არ გაიპარა შეცდომა.
# // raise : სულ იწვევს შეცდომას.


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
        
print(divide(10, 2)) 
print(divide(10, 0))  

try:
    print("Trying...")
except:
    print("Error encountered")
finally:
    print("Code cleanup is done")

def check_password(password):
    try:
        if len(password) < 8:
            raise ValueError("Password too short")
        if " " in password:
            raise ValueError("Password cannot contain spaces")
        return "Password accepted"
    except ValueError as e:
        return str(e)

print(check_password("short"))
print(check_password("pass word"))
print(check_password("StrongPass1"))