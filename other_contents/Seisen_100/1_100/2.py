N=int(input())
 
#https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
 
count=0
for i in range(1, N+1):
  if i%2==1 and len(make_divisors(i))==8:
    count+=1
print(count)
