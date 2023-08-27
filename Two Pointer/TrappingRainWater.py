class Solution:
    def trap(self, height: List[int]) -> int:
        
        right = len(height) - 1
        n = len(height)
        leftbox = [0] * n
        rightbox = [0] * n
        maxLeft = 0
        maxRight = 0
        res = 0

        for i, a in enumerate(height):
            maxLeft = max(maxLeft, a)
            leftbox[i] = maxLeft
            maxRight = max(maxRight, height[right])
            rightbox[right] = maxRight
            right -= 1

        for i in range(len(height)):
            res += min(leftbox[i], rightbox[i]) - height[i]
        
        return res

