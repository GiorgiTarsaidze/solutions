def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for i in range(a, b+1):
        total = 0
        for indx, ele in enumerate(str(i),1):
            total += int(ele)**indx
            if total == i:
                result.append(i)
    
    return result