s=input()
k=int(input())
se=set([s[i:i+k] for i in range(len(s)-k+1)])
print(len(se))
