def bubble_sort(arr):
  flag = True
  while flag:
    flag = False
    for i in range(1, len(arr)):
      if arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1],arr[i]
        flag = True
    
def bubble_sort(arr):
  flag = True
  while flag:
    flag = False
    for i in range(1, len(arr)):
      if arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        flag = True
        
def bubble_sort(arr:List[int])-> None:
  flag = True
  while flag:
    flag = False
    for i in range(1, len(arr)):
      if arr[i]<arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        flag = True
