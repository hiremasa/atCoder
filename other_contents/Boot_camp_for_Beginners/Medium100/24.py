N, A, B = map(int, input().split())

if A > B: exit(print(0))
if N == 1 and A != B: exit(print(0))

mi = (N-1)*A + B
ma = A + (N-1)*B
print(ma - mi +1)