import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Get number of digits, also always returns False on negative numbers and True on 0-9.
        if x >= 10:
            digits = int(math.log10(x))+1
        elif x < 10 and x >= 0:
            return True
        else:
            return False

        for i in range(digits//2):
            # Get the digit in the right for this iteration
            right_digit = x % (10 ** (i+1))
            # Digit in the right must be divided by 10^i
            if i > 0:
                right_digit //= 10 ** i
            # Get the digit in the left for this iteration
            left_digit = x // 10 ** (digits - 1 - i) % 10
            # If they are different we directly return False
            if left_digit != right_digit:
                return False
        
        # Number is a palindrome
        return True
