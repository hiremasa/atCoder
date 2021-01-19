li=input()
n=len(li)
child_li=[0]*n



ruiseki=0
for i in range(n-1):
    if li[i]=='R':
        ruiseki+=1
        if li[i+1]=='L':
            child_li[i+1]=ruiseki//2
            child_li[i]=(ruiseki+1)//2
    else:
        ruiseki=0


ruiseki=0
for i in range(n-1, 0, -1):
    if li[i]=='L':
        ruiseki+=1
        if li[i-1]=='R':
            child_li[i-1]+=ruiseki//2
            child_li[i]+=(ruiseki+1)//2
    else:
        ruiseki=0

print(*child_li)