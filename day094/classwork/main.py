def most_frequent_item_count(arr):
    if len(arr) == 0:
        return 0
    max_count = 1 
    for item in arr:
        count = arr.count(item)
        if count > max_count:
            max_count = count
    return max_count

def count_red_beads(n):
    if n <= 1:
        return 0
    red_beads = (n - 1) * 2
    return red_beads
