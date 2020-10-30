#Program to print the second largest number in a list.

def SLargest(lst):
    largest = None
    SLargest = None
    for i in lst:
        if largest is None:
            largest = i
        elif largest < i:
            SLargest = largest
            largest = i
        else:
            continue    
    return SLargest

lst = list()
size = int(input("How many elements do you want to enter... "))
for i in range(0,size):
    new = input("Enter the next element in the list... ")
    lst.append(new)
print("The original list is: \n",lst)
print("The second largest number in the list is: ",SLargest(lst))
