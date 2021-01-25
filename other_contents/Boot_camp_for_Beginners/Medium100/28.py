import itertools
N, K = map(int, input().split())
E = list(map(lambda x: (int(x)+1)/2, input().split()))

E_acc = list(itertools.accumulate(E))

ans = E_acc[K]- E_acc[0]
for i in range(N-K):
    ans = max(ans, E_acc[i+K]-E_acc[i])
print(ans)