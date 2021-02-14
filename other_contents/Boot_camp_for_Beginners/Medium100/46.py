from collections import Counter
s = input()
c = Counter(s).values()
if (len(c)<3) & (max(c)>1):
    print('NO')
elif (max(c)-min(c)>1):
    print('NO')
else:
    print('YES')



"""
始めに文字aを使うすると、その後ろにはaは置けない。
さらにbを置いてabとすると、この後ろにはc以外を置くことはできない。
abcとなれば同様に必ずaを置かなければならない。
これを繰り返せば、目標の文字列が構成されるならabcabc...abcabとならねばならない。 
よって、入力はそれぞれの文字の数a,b,c∈ℕが与えられるとしてよく、max{a,b,c}≤min{a,b,c}+1が答え。
"""
s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')
result = (max(a, b, c) <= min(a, b, c) + 1)
print(['NO', 'YES'][result])