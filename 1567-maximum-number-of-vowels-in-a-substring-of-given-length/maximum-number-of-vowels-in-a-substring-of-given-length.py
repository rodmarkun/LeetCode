class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr_vowels = 0
        vowels = set('aeiou')
        for letter in s[0:k]:
            if letter in vowels:
                curr_vowels += 1
        max_vowels = curr_vowels
        
        for i in range(1, len(s) + 1 - k):
            if s[i-1] in vowels:
                curr_vowels -= 1
            if s[k - 1 + i] in vowels:
                curr_vowels += 1
                if curr_vowels > max_vowels:
                    max_vowels = curr_vowels
        
        return max_vowels