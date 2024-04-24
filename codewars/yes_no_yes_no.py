def yes_no(arr):
    result = []
    index = 0 
    flag = True

    while arr:
        index %= len(arr)
        if flag:
            result.append(arr.pop(index))
        else:
            index +=1

        flag = not flag

    return result

# Very clever solution:
def yes_no(arr):
    result = []
    while arr:
        result.append(arr.pop(0))
        if arr:
            arr.append(arr.pop(0))
    return result

