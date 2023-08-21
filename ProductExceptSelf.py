class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        product = 1
        for i, num in enumerate(nums):
            res[i] = product
            product = num * product
        product = 1
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] = product * res[i]
            product = nums[i] * product
        
        return res