# def alphabet_war(fight):
#     left = {
#         "w":4,
#         "p":3,
#         "b":2,
#         "s":1,
#         "t":0
#     }
    
#     right = {
#         "m":4,
#         "q":3,
#         "d":2,
#         "z":1,
#         "j":0
#     }
#     left_score = 0
#     right_score = 0
    
#     for letter in fight:
#         if letter in left:
#             left_score += left[letter]
#         elif letter in right:
#             right_score += right[letter]

#     if right_score > left_score:
#         return "Right side wins!"
#     elif left_score > right_score:
#         return "Left side wins!"
#     else:
#         return "Let's fight again!"
    

# print(alphabet_war("jbdt"))