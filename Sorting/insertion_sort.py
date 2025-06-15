"""
we take the anchor element and place it at the right position within the sorted array.

at some point, j and j + 1 will have same element


[1,2,3,5,0]

*************************for better clarity*******************
kind of imagine the position of anchor element is empty
it gives better clarity.
original array: [1,2,3,5,0]

when we take an anchor out. [1,2,3,5, []]
so we immediately fill that out with element 5.

 [1,2,3,[], 5]
 
so now there is an empty element at second last position which is kind of expected to be
filled with our anchor element 

but if anchor element is less than 3 then we might have to replace that hole with 3 not
by anchor element so we need to further check. 

in reality, there will not be a hole but duplicate element even though, we will replace the 
right side element with left side element,both of them will still have same element 
until we replace that with our anchor element 

and we move an element one step to right to fill that whole
when we do that we create another hole
***************************************************************************

element pointed by j = 0

[1,2,3,5,5]
       j  
[1,2,3,3,5]
     j    
[1,2,3,3,5]
   j
[1,2,2,3,5]
 j
[1,1,2,3,5]
j at negative -1
so j++ 
and replace it with anchor value


anchor is still 4
after that j = j - 1 
now j will point to 3
and position of 3 and 5 looks great
so we increment the position of j and add the value of anchor there

so current j points 3 
and incrementing j will point to that duplicate 5.

for thoughts

when loop executes, it means our anchor elements will replace some 
elements in the sorted part of our array but we don't know
however, we will have replaced the position of anchor element with the j value
now element pointed by j and the original position of anchor will have same value.

if no any elements needs further changes we will increment the j which will point to that 
duplicate value and replace it with anchor value as it will be the correct place for 
anchor to stay.

insert sort is all about placing the anchor element in its right position. for that we utilize
j which will initially point to rightmost side of the sorted part of an array and with 
each iteration it will just keep decrementing one step. 


"""

def insertion_sort(arr):
  for i in range(1, len(arr)):
    anchor = arr[i]
    j = i-1
    # checking only till first element.
    # smart algorithm always want to find if another element is greater than anchor
    #if yes create a hole there by shifting that element to right filling previous hole
    while j >= 0 and anchor < arr[j]: #check till the first element if anchor is smallar
      arr[j+1] = arr[j] #needs to replace the j+1 element with jth element as j is larger than anchor
      j = j -1 
      
    # our j is smart, it always attempt to go back one step and check if it finds any element
    #greater than anchor so that it could properly place anchor but if it doesn't find that element
    # it needs to place the anchor in the previous element pointed by j which is 
    # j + 1
    arr[j+1] = anchor
    return arr
      





























































