#Program to print a list after removing all even numbers from it.

def evenRemove(lst):
    for i in lst:
        if i % 2 == 0:
            lst.remove(i)
        else:
            continue
    return lst

lst = list()
size = int(input("How many elements do you want to enter... "))
for i in range(0,size):
    new = int(input("Enter the next element in the list... "))
    lst.append(new)
print("The original list is: \n",lst)
print("The list after removing even numbers is: \n",evenRemove(lst))    
