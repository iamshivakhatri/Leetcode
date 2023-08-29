class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left, right = 0, 0
        deque = collections.deque()
        output = []


        while right < len(nums):

            while deque and deque[-1] < nums[right]:
                deque.pop()
            deque.append(nums[right])

            if (right - left + 1) == k:
                output.append(deque[0])
                #deque[0] means the biggest integer in the deque
                if deque[0] == nums[left]:
                    deque.popleft()
                left += 1

            right += 1
        return output