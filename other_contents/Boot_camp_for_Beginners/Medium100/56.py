import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
N,K,S = map(int,read().split())
 
if S > N:
    A = [S] * K + [1] * (N-K)
else:
    A = [S] * K + [S+1] * (N-K)
 
print(*A)