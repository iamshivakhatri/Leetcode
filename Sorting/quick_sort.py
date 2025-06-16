"""
For brain:

The last  function calling of any branches will be terminated by if statement
So there will be two of those at the end, right

			G

	A			  D
B(Last)	 	C (last)        E	(last) 	F(last)

So any last two branches will have been called by one node  but that node(A or D) will also be 
One of the two branches in its parent function but if this is second last from the actual end nodes, now we reach till the end and return back to its parent and this process happens all the way to the single function which called two functions to start this recursion. 

So one function calls 2 and each will 2 more etc etc like in a tree but at end there should be some conditions to stop that calling so one function stop and another stops and those two return back to the function which called those two and there will be another function just like that 


If you just see a function. It might be a branch. It is only completed when it finds its partner. 
Apart from the main node, there will always be the partner node in this type of recursive calling of two function. 

"""


def quick_sort(arr):
  if len(arr) <= 1:
    return arr 
  
  p = arr[-1]
  
  L = [x for x in arr[:-1] if x <= p]
  R = [x for x in arr[:-1] if x > p]
  
  L = quick_sort(L)
  R = quick_sort(R)
  
  return L + [p] + R
  



