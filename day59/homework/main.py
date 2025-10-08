def other_angle(a, b):
    return 180 - (a + b)



def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a * a + b * b == c * c


def sp_eng(sentence): 
    return 'english' in sentence.lower()


def ensure_question(s):
    if s=="":
        return '?'
    if(s[-1]=='?'):
        return s
    else:
        return s+'?'
    
def switch_it_up(number):
    if number == 1:
        return"One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
    elif number == 0:
        return "Zero"
    else:
        return "i have depression please help"
    

def position(alphabet):
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return "Position of alphabet: " + "".join(str(x+1) for x in range(len(alpha)) if alpha[x]==alphabet)