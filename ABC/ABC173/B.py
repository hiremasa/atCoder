from collections import Counter
n=int(input())
 
dic=[""]*n
 
for i in range(n):
  dic[i]=str(input())
 
cnt=Counter(dic)
 
lookup=["AC", "WA", "TLE", "RE"]
for i in lookup:
  print(i, " x ",cnt[i]) 