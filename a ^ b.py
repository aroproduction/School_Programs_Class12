# power a to b using iteration

def power(a, b):
    res = 1
    if b == 0:
        return 1
    else:
        for i in range(b):
            res *= a
        return res


print("Enter only the positive numbers below")
num = int(input("Enter base number: "))
p = int(input("raise to power of: "))
result = power(num, p)
print(num, "raised to power of", p, "is", result)
