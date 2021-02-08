import sys
input = sys.stdin.readline
 
S = input().rstrip()
 
def F(S,target):
    cnt = 0
    while S.count(target) != len(S):
        cnt += 1
        S = ''.join(y if x != target else x for x,y in zip(S[:-1],S[1:]))
    return cnt
 
answer = min(F(S,t) for t in set(S))
print(answer)