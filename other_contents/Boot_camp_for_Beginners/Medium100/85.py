S = input()
se_S = set(S)

if len(S) < 26:
    ans = S + min([s for s in set("abcdefghijklmnopqrstuvwxyz") if s not in set(S)])
else:
    bools = []
    for i in range(25):
        bools.append(S[i] > S[i + 1])

    if all(bools):
        ans = -1
    else:
        idx = 0
        for i, bl in enumerate(bools):
            if not bl:
                idx = i
        ans = S[:idx] + min([s for s in set(S[idx + 1:]) if s > S[idx]])
print(ans)

