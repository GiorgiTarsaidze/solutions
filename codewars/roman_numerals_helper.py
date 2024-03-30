# class RomanNumerals:
#     @staticmethod
#     def to_roman(val : int) -> str:
        
        
        
#         return ''

#     @staticmethod
#     def from_roman(roman_num : str) -> int:
        
        
#         return 0


numbers = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

def from_roman(roman_num : str) -> int:
    result = 0
    for i in roman_num:
        print(numbers[i])
        
    return 0


from_roman("MDCLXVI")