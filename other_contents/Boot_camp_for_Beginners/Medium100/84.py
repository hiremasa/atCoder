from bisect import bisect_left, bisect_right

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i in range(N - 2):
    a = L[i]
    for j in range(i + 1, N - 1):
        b = L[j]

        idx1 = bisect_left(L[j + 1:], b - a + 1)
        idx2 = bisect_right(L[j + 1:], a + b - 1)
        ans += max(0, idx2 - idx1)
print(ans)