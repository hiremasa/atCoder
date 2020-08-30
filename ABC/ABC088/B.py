N=int(input())
A=sorted(list(map(int, input().split())), reverse=True)

bob=sum(A[1::2])
alice=sum(A[::2])


print(alice-bob)