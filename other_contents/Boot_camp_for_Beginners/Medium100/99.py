N,M,K = map(int,input().split())

for n in range(N + 1):
    for m in range(M + 1):
        temp = n * (M - m) + m * (N - n)
        if temp == K:
            exit(print("Yes"))
print("No")