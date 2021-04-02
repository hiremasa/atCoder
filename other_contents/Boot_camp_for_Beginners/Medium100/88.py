x = int(input())
f = lambda x: max(set([range(1, 7)]) - set([x, 6- x]))
ans = total = 0
now = 6
while total < x:
    ans += 1
    next_ = f(now)
    total += next_
    now = next_
print(ans)


x = int(input())
print(x // 11 * 2 + (0 if x % 11 == 0 else (1 if x % 11 <= 6 else 2)))