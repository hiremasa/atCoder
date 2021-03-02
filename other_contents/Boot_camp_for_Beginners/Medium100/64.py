from collections import Counter

N = int(input())
c = Counter(int(x) for x in input().split())

answer = 0

for k,v in c.items():
  if k <= v:
    answer += v-k
  else:
    answer += v
print(answer)


