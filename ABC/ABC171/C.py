N=int(input())
ans=""
check="abcdefghijklmnopqrstuvwxyz"

while N!=0:
	N-=1
	ans+=check[N%26]
	N=N//26

print(ans[::-1])
"""
while N>0:
	N-=1
	ans+=chr(ord("a")+ N%26)
	N//=26
print(ans[::-1])
"""


