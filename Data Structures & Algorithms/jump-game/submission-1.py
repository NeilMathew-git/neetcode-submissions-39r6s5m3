class Solution:
    def canJump(self, nums: List[int]) -> bool:
        life = 0
        for i in range(len(nums)):
            if life < 0:
                return False
            life = max(life, nums[i])
            life -= 1
            
        return True


        