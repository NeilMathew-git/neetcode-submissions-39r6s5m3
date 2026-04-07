class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        elements = set(nums)
        for i in nums:
            if i - 1 not in nums:
                curr = i 
                length = 1
                while curr + 1 in elements:
                    length += 1
                    curr += 1
                longest = max(longest, length)
        return longest

        