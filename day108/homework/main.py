def hello(name):
    return f'Hello, {name}'

def goodbye(name):
    return f'Goodbye, {name}'

def process_user(name, func):
    return func(name)

print(process_user('Deme', hello))
print(process_user('Deme', goodbye))

# Built-in functions : print(), len(), type()
# User-defined functions : def
# Anonymous : Lambda functions


print(len("Python"))
print(type(10))

def add(a, b):
    return a + b
def greet(name):
    return f"Hi, {name}"

square = lambda x: x * x
multiply = lambda a, b: a * b


def validate_password(password):

    def has_min_length():
        return len(password) >= 8

    def has_digit():
        return any(char.isdigit() for char in password)

    def has_uppercase():
        return any(char.isupper() for char in password)

    return has_min_length() and has_digit() and has_uppercase()
