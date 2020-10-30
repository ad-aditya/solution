#Program to find the nth number of the Fibonacci series and also its factorial.

def nFib(n):
    data = list()
    fib = list()
    n1, n2 = 0, 1
    count = 0

    if n <= 0:
       print("Please enter a positive integer")
    elif n == 1:
       fib.append(n1)
    else:
       while count < n:
           fib.append(n1)
           temp = n1 + n2
           n1 = n2
           n2 = temp
           count += 1
    nth = fib[-1]
    data.append(nth)
    fact = 1
    if nth == 0 or nth == 1:
        fact = 1
    else:
        while nth >= 1:
            fact *= nth
            nth -= 1
    data.append(fact)
    return data

n = int(input("Enter the number to find the nth number in the Fibonacci series and the factorial of the number... "))
print("The",n,"th number in the Fibonacci series and its factorial respectively are..",nFib(n))
