class Solution:
   def maxSubArray(self, nums: List[int]) -> int:
       max_sum = curr_sum = nums[0]
       for val in nums[1:]:
           curr_sum = max(curr_sum+ val, val )
           max_sum = max(curr_sum, max_sum)
       return max_sum

