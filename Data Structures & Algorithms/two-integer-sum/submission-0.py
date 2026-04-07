class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = set()
        for i in range(len(nums)):
            
            if target - nums[i] in visited:
                return [nums.index(target - nums[i]), i]
                
            visited.add(nums[i])