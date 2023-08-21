class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creating a dictionary to store frequency
        freqMap = {}
        for i in nums:
            freqMap[i] = freqMap.get(i, 0)+1

        #creating a list which has list as its elements

        myList = [[] for i in range(len(nums)+1)]

        #creating an array to give an output
        res = []   

        #iterating over a hashmap
        for key, value in freqMap.items():
            myList[value].append(key)

        #backward looping the myList 
        for i in range(len(myList)-1, 0,-1):
            #looping the inner list to store the elements
            for j in myList[i]:
                res.append(j)
                if len(res) == k:
                    return res

#o(n)

#Here we are creating the list which contains frequency as index and its value as the element which has that frequencey.

         

                