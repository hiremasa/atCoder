N= int(input())
A = list(map(int, input().split()))

from collections import Counter
C = sorted(Counter(A).items(), key=lambda x: x[0], reverse=True)

ll2 = [0, 0]
ll4 = [0, 0]
cnt = 0
for k, v in C:
    if v >= 4:
        ll4[0] = k
        ll4[1] = k
        break
for k, v in C:
    if v >= 2:
        ll2[cnt] = k
        cnt += 1
        if cnt >=2:
            break
print(max(ll4[0] * ll4[1], ll2[0] * ll2[1]))
