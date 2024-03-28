class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ocurrences = {}
        left = 0
        max_len_subarray = 0
        for right in range(len(nums)):
            if ocurrences.get(nums[right]) is None:
                ocurrences[nums[right]] = 1
            else:
                ocurrences[nums[right]] += 1
            if ocurrences[nums[right]] > k:
                while ocurrences[nums[right]] > k and left < right:
                    ocurrences[nums[left]] -= 1
                    left += 1
            if (right + 1) - left > max_len_subarray:
                max_len_subarray = (right + 1) - left
        return max_len_subarray