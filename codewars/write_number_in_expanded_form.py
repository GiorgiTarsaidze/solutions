def expanded_form(num):
    length = len(str(num))-1
    result_num = ''

    for i in str(num):
        if i == '0':
            length -= 1
            continue
        result_num += str(int(i) * 10 ** (length)) + " + "
        length -= 1

    return result_num[:-3]
