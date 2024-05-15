class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correspondences = {")": "(", 
                           "}" : "{", 
                           "]": "["
                          }
        for letter in s:
            if letter in ["(", "{", "["]:
                stack.append(letter)
            elif letter in correspondences.keys():
                if len(stack) > 0 and correspondences[letter] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
                
            