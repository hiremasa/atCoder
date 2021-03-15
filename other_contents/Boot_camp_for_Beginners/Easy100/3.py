N,A,B = map(int,input().split())
S = input()

total = 0
b = 0
answer = []

for s in S:
  bl = False
  if s == 'a':
    if total < A+B:
      bl = True
      total += 1
  elif s == 'b':
    if total < A+B and b < B:
      bl = True
      total += 1
      b += 1
  answer.append('Yes' if bl else 'No')

print(*answer, sep='\n')
