import random

a = [100, 200, 300, 400, 500]
l = random.randint(1, 3)
u = random.randint(2, 4)
for k in range(l, u):
    print(a[k], end=";")
