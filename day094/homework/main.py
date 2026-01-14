def is_square(n):
    if n < 0:
        return False

    root = int(n ** 0.5)
    if root * root == n:
        return True
    else:
        return False

def sum_of_minimums(numbers):
    total = 0

    for row in numbers:
        smallest = min(row)
        total = total + smallest

    return total

def square_digits(num):
    result = ""

    for digit in str(num):
        digit = int(digit)
        squared = digit * digit
        result = result + str(squared)

    return int(result)

def remove_url_anchor(url):
    if "#" in url:
        return url.split("#")[0]
    else:
        return url

def angle(n):
    return 180 * (n - 2)
