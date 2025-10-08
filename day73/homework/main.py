def get_average(marks):
    total = sum(marks)        
    count = len(marks)        
    average = total / count   
    return int(average) 

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    if p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    if p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    
def plural(n):
    if n == 1:
        return False
    else:
        return True
    
def bonus_time(salary, bonus):
    if bonus == True:
        total = salary * 10
    else:
        total = salary
    return "$" + str(total)

def say_hello(name):
    return "Hello, " + name