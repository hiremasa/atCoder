from collections import Counter
N = int(input())
V = list(map(int, input().split()))

EV_counter = Counter(V[::2])
OD_counter = Counter(V[1::2])
 
# 1種類しかないとき対策
EV_counter[-1] = 0
OD_counter[-2] = 0
 
# 上位2種しか使う必要がない
EV = EV_counter.most_common(2)
OD = OD_counter.most_common(2)
 
answer = N
for (k1,v1), (k2,v2) in itertools.product(EV,OD):
    if k1 == k2:
        continue
    x = (N - v1 - v2)
    if answer > x:
        answer = x

print(answer)



V_odd = V[0::2]
V_even = V[1::2]
print(Counter(V_odd), Counter(V_even))
c_odd = sorted(dict(Counter(V_odd)), key=lambda x: x[1], reverse=True)
c_even = sorted(dict(Counter(V_even)), key=lambda x: x[1], reverse=True)

ans = 0

for i, k, v in enumerate(c_odd.items()):
    if i == 0:
        continue
    ans += v

for i, k, v in enumerate(c_even.items()):
    if i == 0:
        continue
    ans += v
print(ans)