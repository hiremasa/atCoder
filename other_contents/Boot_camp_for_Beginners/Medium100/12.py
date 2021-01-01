H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]

B = list(zip(*[i for i in A if "#" in i]))

C = list(zip(*[j for j in B if "#" in j]))

for i in range(len(C)):
    print(*C[i], sep="")
