N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
BC=[tuple(map(int,input().split())) for _ in range(M)]
BC.sort(key=lambda x:x[1],reverse=True)
now=0
for i in range(M):
    for j in range(BC[i][0]):
        if now>=N:
            break
        elif A[now]<BC[i][1]:
            A[now]=BC[i][1]
            now+=1
        else:
            break
    else:
        continue
    break
print(sum(A))