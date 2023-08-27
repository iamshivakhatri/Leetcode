class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        maxArea = 0
        left = 0
        right = len(height) - 1

        while(left < right):
            area = (right - left) * max(height[right], height[left])
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
            maxArea = max(area, maxArea)

        return maxArea
