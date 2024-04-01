def strip_comments(strng, markers):
    lst = strng.split("\n")
    
    modified_lst = []
    
    for line in lst:
        for marker in markers:
            if marker in line:
                line = line[:line.index(marker)].rstrip()
                break
        modified_lst.append(line)

    return "\n".join(modified_lst)