N = int(input())
A = list(map(int, input().split()))
A_abs = [abs(a) for a in A]
neg_cnt = 0
flag = False

for i in range(N):
    a = A[i]

    if a < 0:
        neg_cnt += 1
    elif a == 0:
        flag = True

if flag or neg_cnt % 2 == 0:
    ans = sum(A_abs)
else:
    ans = sum(A_abs) - 2 * min(A_abs)
print(ans)