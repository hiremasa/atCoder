N = int(input())
S = input()
import itertools
acc_left = [0]
for i in range(N):
    if S[i] == "W":
        acc_left.append(1)
    else:
        acc_left.append(0)
acc_left = list(itertools.accumulate(acc_left))


acc_right = [0]
for i in range(1, N + 1):
    if S[N - i] == "E":
        acc_right.append(1)
    else:
        acc_right.append(0)
acc_right = list(itertools.accumulate(acc_right))[::-1]

ans = float("inf")
for i in range(N):
    ans = min(ans, acc_left[i] + acc_right[i + 1])
print(ans)