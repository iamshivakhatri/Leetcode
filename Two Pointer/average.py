print("Enter five numbers: ")
sum = 0

for i in range(5):
    num  = int(input(f"Enter number {i+1} "))
    sum = sum + num
print("Average is ", sum/5)


