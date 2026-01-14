def excluding_vat_price(price, vat):
    if price == 0:
        return 0
    return round(price / (1 + vat/100), 2)

def flick_switch(lst):
    state = True
    result = []
    for item in lst:
        if item == "flick":
            state = not state
        result.append(state)
    return result

def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else: 
        return 4


def quarter_of(month):
    return (month - 1) // 3 + 1


def warn_the_sheep(queue):
    pos = queue.index("wolf")
    if pos == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
    return f"Oi! Sheep number {len(queue) - pos - 1}! You’re about to be eaten by a wolf!"
