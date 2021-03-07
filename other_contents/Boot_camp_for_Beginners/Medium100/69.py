import math
N = int(input())
A = [int(input()) for _ in range(5)]
print(math.ceil(N/min(A)) + 4)
