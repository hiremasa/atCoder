from collections import Counter
N=int(input())
A=list(map(int, input().split()))

cnt=Counter(A)
print("YES" if all([i==1 for i in cnt.values()]) else "NO")