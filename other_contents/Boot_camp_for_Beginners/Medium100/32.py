N, Y = map(int, input().split())
Y //= 1000

"""
10a + 5b + 1c = Y//1000
a + b + c = N
"""
for a in range(Y//9 + 1):
    for b in range((Y-a*9)//4 + 1):
        if a + b <= N and 9*a + 4*b == Y - N:
                exit(print(a, b, N-a-b))
print(-1, -1, -1)
