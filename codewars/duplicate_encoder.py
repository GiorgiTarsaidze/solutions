def duplicate_encode(word):
    #your code here
    result = ""
    for i in word.lower():
        if word.lower().count(i) > 1:
            result += ")"
        else:
            result += "("
    
    return result