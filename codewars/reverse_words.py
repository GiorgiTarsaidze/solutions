def reverse_words(text):
  #go for it
    txt_lst = text.split(" ")
    return " ".join([i[::-1] for i in txt_lst])