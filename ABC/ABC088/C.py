C=[list(map(int, intput().split()) for _ in range(3))]

# a1 = 0としてよい

A = [0,None,None]
B = [None,None,None]

bl = True
for i in range(3):
  C = [int(x) for x in input().split()]
  for j,c in enumerate(C):
    if A[i] is None:
      A[i] = c - B[j]
    if B[j] is None:
      B[j] = c - A[i]
    if A[i]+B[j] != c:
      bl = False

answer = 'Yes' if bl else 'No'
print(answer)
