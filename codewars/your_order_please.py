def order(sentence):
  # code here
  return " ".join(sorted(sentence.split(" "), key=lambda word: [int(letter) for letter in word if letter.isdigit()]))
