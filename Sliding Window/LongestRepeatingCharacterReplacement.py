class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        alpharray = [0] * 26
        aPointer = 0
        bPointer = 0
        maxLength = 0
        frequent = 0


        for i, a in enumerate(s):
            alpharray[ord(a)- ord('A')] += 1
            frequent = max(frequent, alpharray[ord(a)- ord('A')])

            #Breaking the loop if there is more number of character to be change in the sliding window than the value of k.

            if (bPointer - aPointer + 1 ) - frequent > k:
                alpharray[ord(s[aPointer])- ord('A')] -= 1
                aPointer += 1

            #This will not be updated unless there is another sliding window which is bigger than the current biggest one
            maxLength = max(maxLength, bPointer - aPointer + 1)
            bPointer += 1
        

        return maxLength

        """
        This is classic case of sliding window problem
        1. Here both aPointer and bPointer points out to the 0 index at first
        2.bPointer gradually increases which increases the length of the sliding window
        3.now we should shrink the sliding window based on a condition
        4. if sliding window has less no of frequent then it means more character needs to be change now.
        5. We should check it with k and shrink the window

        Tricky thing is frequent is not updated when aPointer is updated. but there is no need to update the frequent as it won't have any impact on maxLength. It will hold the same frequent value even though all the characters are not in the sliding window. It will change only when same character is repeated more or some other character is now frequently presented.

        """
 