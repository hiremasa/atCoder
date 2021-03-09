import itertools
N = int(input())
A = list(map(int, input().split()))
A_acc = list(itertools.accumulate(A))
print(A_acc)
ans = float("inf")
last = A_acc[-1]
for a_acc in A_acc[:-1]:
    ans = min(abs(last - 2 * a_acc), ans)
print(ans)
