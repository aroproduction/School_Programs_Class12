# Default Fibonacci Numbers using Recursion

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# __main__
n = int(input("Enter the last term: "))
for i in range(1, n+1):
    print(fib(i), end=", ")
