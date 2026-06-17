class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        visited = set(range(len(nums) + 1))
        print(visited)
        for i in nums:
            visited.remove(i)
        for i in visited:
            return i
        