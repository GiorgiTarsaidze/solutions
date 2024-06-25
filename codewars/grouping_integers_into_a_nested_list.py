def group_ints(lst, key):
    result = []
    current = [lst[0]]

    for i in range(1, len(lst)):
        if (lst[i-1] < key and lst[i] < key) or (lst[i-1] >= key and lst[i] >= key):
            current.append(lst[i])
        else:
            result.append(current)
            current = [lst[i]]
    result.append(current)

    return result
