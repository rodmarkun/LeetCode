class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Check for empty string
        if len(s) > 0:
            # Initializate the longest substring variable
            longest_substring = s[0]

            # Iterate through each letter
            for idx, letter in enumerate(s):
                # Create a current substring
                curr_substring = letter
                # For each subsequent letter following the actual one
                for cont_letter in s[idx+1:]:
                    # Add to substring and check for the longest if it doesn't include it yet
                    if cont_letter not in curr_substring:
                        curr_substring += cont_letter
                        if len(curr_substring) > len(longest_substring):
                            longest_substring = curr_substring
                    # If it is, break this cycle
                    else:
                        break
            # Returns the length of the longest substring found
            return len(longest_substring)
        else:
            return 0
        