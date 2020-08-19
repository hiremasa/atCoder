N=int(input())

print((1+N//1000)*1000-N if N%1000!=0  else 0)