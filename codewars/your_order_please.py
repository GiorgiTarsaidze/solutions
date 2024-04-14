def order(sentence):
  # code here
  lst_sentance = sentence.split(" ")
  result = sorted(lst_sentance, key=lambda word: [int(letter) for letter in word if letter.isdigit()])
  return " ".join(result)
