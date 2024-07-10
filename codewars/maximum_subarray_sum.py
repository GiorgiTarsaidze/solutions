def max_sequence(arr):
    if not arr:
        return 0
    current_max = 0
    global_max = 0
    
    for number in arr:
        current_max = max(number, current_max + number)
        global_max = max(global_max, current_max)
    return global_max
