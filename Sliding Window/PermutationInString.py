class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         #array for string s1
        s1array = [0] * 26

        #array for the string s2
        s2array = [0] * 26

        for i, a in enumerate(s1):
            s1array[ord(a) - ord('a')] += 1

        windowL = len(s1)

        left, right = 0,0
        for i, a in enumerate(s2):
            s2array[ord(a)- ord('a')] += 1
            if (right - left)+ 1 == windowL:
                if s1array == s2array:
                    return True
                s2array[ord(s2[left])- ord('a')] -= 1
                left += 1
            right += 1
        return False


        """
        Classic case of sliding window problem

        1. we are creating two arrays same to the both string
        2. we will create a sliding window of length equaling to the string s1
        3. if window length matches to the first string then we will check if both array are equal or not
        4. if array doesn't equal then we won't increase the length of the array now and the length of sliding window will also be same
        5. we will remove the element from the left
     """