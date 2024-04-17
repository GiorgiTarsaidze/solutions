def is_pangram(s):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    letter_dir = {}
    
    for letter in alphabet:
        letter_dir[letter] = 0
        
    for i in s:
        if i.lower() in letter_dir:
            letter_dir[i.lower()] += 1

    if 0 in set(letter_dir.values()):
        return False
    
    return True

