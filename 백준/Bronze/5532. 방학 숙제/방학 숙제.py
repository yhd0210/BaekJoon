import math
n = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
a = math.ceil(n1 / n3)
b = math.ceil(n2 / n4)
c = max(a, b)
print(n - c)