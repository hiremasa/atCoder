N = int(input())
b = list(map(int,input().split()))
ans = []
for i in range(N):
    for j in range(len(b)-1,-1,-1):
        if b[j] == j+1:
            b.pop(j)
            ans.append(j)
            break
        if j == 0:
            print(-1)
            exit()
for i in range(N-1,-1,-1):
    print(ans[i]+1)