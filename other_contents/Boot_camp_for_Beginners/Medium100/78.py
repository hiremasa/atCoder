from itertools import groupby
 
 
def solve(s, k):
    rle = [len(list(g)) for c, g in groupby(s)]
    if len(rle) == 1:
        return len(s) * k // 2
    ans = sum(l // 2 for l in rle) * k
    if s[0] == s[-1] and rle[0] % 2 == 1 and rle[-1] % 2 == 1:
        ans += k - 1
    return ans
 
 
s = input()
k = int(input())
print(solve(s, k))