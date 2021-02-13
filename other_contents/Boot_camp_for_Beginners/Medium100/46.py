from collections import Counter
s = input()
c = Counter(s).values()
if (len(c)<3) & (max(c)>1):
    print('NO')
elif (max(c)-min(c)>1):
    print('NO')
else:
    print('YES')