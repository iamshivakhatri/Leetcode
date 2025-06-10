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
    
def insertion_sort(arr):
  for i in range(1, len(arr)):
    anchor = arr[i]
    j = i-1
    while j >=0 and anchor < arr[j]:
      arr[j+1] = arr[j]
      j -= 1 
    arr[j+1] = anchor
