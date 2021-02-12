N, M = map(int, input().split())
sccs = (N * 2 + M) // 4
if N <= sccs:
  print(sccs)
else:
  print(M // 2)