from collections import Counter

N = int(input())
S = [Counter(input()) for _ in range(N)]
SC = S[0]
for i in range(1, N):
    for k, v in SC.items():
        SC[k] = min(S[i][k], SC[k])

SC = sorted(SC.items())
answer = ''
for k,v in SC:
  answer += k*v
print(answer)
