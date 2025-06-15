

"""
Bubble Sort:
Time: O(N^2)
Space: O(1)


it is nested loop

it is constant iteration from first element to last element
and for every iteration within the list it grabs the highest element and then place it 
at the right side

if in a single iteration, if it doesn't even interchange one position then it means
array is sorted.

[2,1,3,4]
very simple algorithm

flag = False
we default assume an array is sorted and even if we find it is not we flag it True
so that we can come back again

flag = True
we set this True so that we can run the while looop again. 
flagging True doesn't mean it requires further sorting. it just opens the possibility
to run while loop again, it will check again if it needs interchanging if not flag will be
false by default when we run the while loop.

story:
we will atleast run through all the elements in the array and try to interchange it if
we interchange it once we flag true so that we can activate while loop if we don't even
interchange one element that means our list is sorted and flag remains false and we don't 
even come back once after full iteration of for loop. 
"""


def bubble_sort(arr):
  flag = True
  while flag:
    flag = False
    for i in range(1, len(arr)):
      if arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1],arr[i]
        flag = True
  return arr

  
bubble_sort()


