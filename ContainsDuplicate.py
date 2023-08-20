class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        