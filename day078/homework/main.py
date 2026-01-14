def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()

def find_needle(haystack):
    for i in range(len(haystack)):
         if haystack[i] == "needle":
                return "found the needle at position " + str(i)
         
def how_many_light_sabers_do_you_own(name=""):
    if name == "Zach":
        return 18
    else:
        return 0
    

def open_or_senior(data):
    result = []
    for person in data: 
        age = person[0]
        handicap = person[1]
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    
    return result