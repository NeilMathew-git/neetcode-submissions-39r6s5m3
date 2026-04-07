class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        elements = set(numbers)
        for i in numbers:
            complement = target - i
            if complement in elements:
                return [numbers.index(i) + 1, numbers.index(complement) + 1]