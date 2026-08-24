class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_A = 0

        while left < right:
            area = (right - left) * heights[left] if heights[left] < heights[right] else (right - left) * heights[right]
            
            max_A = max(max_A, area) 
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_A