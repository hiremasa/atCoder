S = input()
N = len(S)
L = [1 if c=="L" else 0 for c in S]
R = [1 if c=="R" else 0 for c in S]
Ans = [0] * N
for i, c in enumerate(S):
    if c=="R":
        if S[i+1]=="L":
            Ans[i] += R[i]
        else:
            R[i+2] += R[i]
    else:
        Ans[i] += R[i]

for i, c in zip(range(N-1, -1, -1), S[::-1]):
    if c=="L":
        if S[i-1]=="R":
            Ans[i] += L[i]
        else:
            L[i-2] += L[i]
    else:
        Ans[i] += L[i]

print(" ".join(map(str, Ans)))
