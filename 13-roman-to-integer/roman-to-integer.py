class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
        
        number = 0
        for idx in range(len(s) - 1):
            numerical_value = symbols[s[idx]]
            next_numerical_value = symbols[s[idx + 1]]
            
            if numerical_value < next_numerical_value:
                number -= numerical_value
            else:
                number += numerical_value
                
        number += symbols[s[-1]]
                
        return number