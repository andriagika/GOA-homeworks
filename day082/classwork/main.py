def array(string):
    parts = string.split(',')
    middle = parts[1:-1]
    if not middle:
        return None
    return " ".join(middle)
