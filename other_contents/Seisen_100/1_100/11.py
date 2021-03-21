import itertools
N, M = map(int, input().split())
Sn = []
for _ in range(M):
    Sn.append(list(map(int, input().split()))[1:]) #0-indexにkがある
P = list(map(int, input().split()))

ans = 0
for bools in itertools.product([True, False], repeat=N):
    cnt = 0
    for i, S in enumerate(Sn):
        if len(set([j + 1 for j in range(N) if bools[j]]) & set(S)) % 2 == P[i]:
            cnt += 1
    if cnt == M:
        ans += 1
print(ans)