class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from math import prod
        product = 1
        for i in nums:
            product *= i

        
        output = []
        for i in nums:
            if i != 0:
                num = int(product/i)
            else:
                new_nums = nums[:]
                new_nums.remove(0)
                num = math.prod(new_nums)
            output.append(num)
        return output