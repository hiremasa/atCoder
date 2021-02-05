K, A, B = map(int, input().split())

change = (B - A) > 2
 
bisket = 1
t = min(A-1,K)
bisket += t
K -= t
if not change:
    bisket += K
else:
    q,r = divmod(K,2)
    bisket += (B-A) * q + r
 
print(bisket)