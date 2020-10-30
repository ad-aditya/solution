#Program to print the digits of a number >= 10 as a set.

def setD(num):
    digSet = set()
    for i in num:
        digSet.add(int(i))
    return digSet

n = input("Enter a number to print its digits as a set... ")
print("The digits of the number as a set are...\n",setD(n))
