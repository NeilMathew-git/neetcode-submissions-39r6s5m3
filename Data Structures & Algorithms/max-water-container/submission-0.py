class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        max_water = 0 
        while left < right:
            left_bin_height = heights[left]
            right_bin_height = heights[right]
            width = right - left
            area = min(left_bin_height, right_bin_height) * width
            max_water = max(max_water, area)
            if left_bin_height < right_bin_height:
                left += 1
            elif left_bin_height >= right_bin_height:
                right -= 1 
        return max_water
            
        