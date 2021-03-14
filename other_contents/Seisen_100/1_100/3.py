S = input()

ans = 0
cnt = 0
for s in S:
    if s in ["A", "T", "G", "C"]:
        cnt += 1
        ans = max(ans, cnt)

    else:
        cnt = 0
print(ans)