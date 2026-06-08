class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]
        for i in nums[1:]:
            if i > curr:
                if curr > 0:
                    curr += i
                else:
                    curr = i
            else:
                curr += i
            best = max(best, curr)
        return best
            
        