def number(lines):
    result = []
    enumerated_lst = enumerate(lines, 1)
    for i in enumerated_lst:
        result.append(f"{i[0]}: {i[1]}")
    return result