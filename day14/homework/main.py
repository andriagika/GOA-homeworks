
# Boolean მნიშვნელობები (True და False)

print(True and True) # Ouput: True
print(True and False) # Ouput: False
print(False and True) # Ouput: False
print(False and False) # Ouput: False

print(True or True) # Ouput: True
print(True or False) # Ouput: True
print(False or True) # Ouput: True
print(False or False) # Ouput: False

print(False or True and True and False) #False

print(True and False or False or True) #True

print(True or True and False or True or False and True or False) #True

house_temp = float(input("What's the temperature?: "))
print(house_temp > 30)

temp = float(input("Enter temperature in celcius: "))
farenheit = (temp * 9/5) + 32
print(farenheit > 89.6)
 