class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_number = 0
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
            
        return x == reversed_number or x == reversed_number // 10
        
        # Converting to string
        # num_string = str(x)
        # pal = True
        # for i in range(len(num_string) // 2):
        #    if num_string[i] != num_string[len(num_string) - 1 - i]:
        #        pal = False
        #        break
        # return pal