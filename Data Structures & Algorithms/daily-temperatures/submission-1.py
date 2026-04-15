class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pairs stored as (temp, index)
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = index - stackInd
            stack.append((temp, index))
        return res