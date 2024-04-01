def pig_it(text):
    lst = text.split()
    result_lst = []
    for element in lst:
        if element.isalpha() == False:
            result_lst.append(element)
            continue
        first_letter = element[0]
        modified_element = element[1:]
        modified_element += f"{first_letter}ay"
        result_lst.append(modified_element)

    return " ".join(result_lst)
