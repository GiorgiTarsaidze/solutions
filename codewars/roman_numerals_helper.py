class RomanNumerals:
    
    numbers = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
        "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
        "V": 5, "IV": 4, "I": 1
    }
    
    @staticmethod
    def to_roman(val : int) -> str:
        result = ""

        sorted_numbers = sorted(RomanNumerals.numbers.items(), key=lambda x: x[1], reverse=True)

        for letter, number in sorted_numbers:
            while val >= number:
                result += letter
                val -= number

        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        result = 0
        for i in range(len(roman_num)):
            if i + 1 < len(roman_num) and RomanNumerals.numbers[roman_num[i]] < RomanNumerals.numbers[roman_num[i+1]]:
                result -= RomanNumerals.numbers[roman_num[i]]
            else:
                result += RomanNumerals.numbers[roman_num[i]]

        return result