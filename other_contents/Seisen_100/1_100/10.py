import itertools
N = int(input())
Q = list(map(int, input().split()))
A = int(input())
M = list(map(int, input().split()))


yes_nums = set()

for bools in itertools.product([True, False], repeat =N):
    yes_nums.add(sum(Q[i] for i in range(N) if bools[i]))


for m in M:
  print("yes" if m in yes_nums else "no")