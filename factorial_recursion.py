# recursive code to calculate the factorial of a number

def factorial(n):
    if n == 1:           
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number (>0): "))
print("Factorial of", n, "is", factorial(n))
