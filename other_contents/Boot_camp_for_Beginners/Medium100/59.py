N=int(input())
p=list(map(int,input().split(" ")))
i=0
c=0
while i<N:
    if p[i]==i+1:
        if i<N-1 and p[i+1]==i+2:
            c+=1
            i+=1
        else:
            c+=1
    i+=1

print(c)