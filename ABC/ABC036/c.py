N=int(input())
A=[int(input()) for _ in range(N)]

se=set(A)
li=sorted(se)
num_to_idx={x:i for i, x in enumerate(li)}

for a in A:
  print(num_to_idx[a])
