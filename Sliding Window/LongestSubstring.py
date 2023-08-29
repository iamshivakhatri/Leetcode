class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aPointer = 0
        bPointer = 0
        mySet = set()
        maxLength = 0


        while bPointer < len(s):
            if s[bPointer] not in mySet:
                mySet.add(s[bPointer])
                bPointer += 1
            else:
                mySet.remove(s[aPointer])
                aPointer += 1
            maxLength = max(len(mySet), maxLength)
        return maxLength
            
            

"""
This is the classic case of sliding window problem
1. you assign aPointer and bPointer to both at the first index of the string
2. you keep on moving bPointer if you find non-repeating elements.
3. if you find repeating element you remove the first element and increment aPointer
4. use the hashset to store the character.
"""