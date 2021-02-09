S = input()
N = len(S)

#========================TLE========================
def step(i, j):
    if i < j:# 上行く
        if S[i]=="U":
            return 1
        else:
            return 2
    elif i> j:# 下行く
        if S[i]=="D":
            return 1
        else:
            return 2


ans = sum([step(i, j) for i in range(N) for j in range(N) if i != j])
print(ans)


#========================AC========================
"""
S[i] == Uのとき
    自分より上の階の個数 * 1
    自分より下の階の個数 * 2
S[i] == Dのとき
    自分より上の階の個数 * 2
    自分より下の階の個数 * 1

自分より上の階の個数 = N - i - 1
自分より上の階の個数 = i 
"""

ans = 0
for i in range(N):
    if S[i] == "U":
        ans += 1 * (N - i - 1) + 2 * i
    else:
        ans += 2 * (N - i - 1) + 1 * i
print(ans)
