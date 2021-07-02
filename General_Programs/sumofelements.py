def sum(l, n):
    if n == 0:
        return l[0]
    else:
        return l[n] + sum(l, n-1)


list1 = [10, 20, 30, 40, 50, 60, 70]
size = len(list1)
print("Sum =", sum(list1, size-1))
