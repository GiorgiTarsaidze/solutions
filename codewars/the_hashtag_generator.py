def generate_hashtag(s):
    final_str = "#"+s.strip().title().replace(" ", "")
    if len(final_str)>140:
        return False
    elif s == "" or final_str == "":
        return False
    
    return final_str