#Program to compute the value of the given series.

from q3 import factorial

def series(x,n):
    sum_series = 0
    i = 0
    for term in range(1,n+1):
        if term % 2 == 1:
            sum_series += (x**i)/factorial(i)
        else:
            sum_series -= (x**i)/factorial(i)
        i += 2
    return sum_series

x = int(input("Enter the value of x- "))
n = int(input("Enter the number of terms you want to compute the series for- "))
print("Sum: ",series(x,n))
