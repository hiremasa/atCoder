x = int(input())

def f(x):
    return max(set([1, 2, 3, 4, 5, 6]) - set([x, 6 - x]))
ans = total = 0
now = 4
while total < x:
    ans += 1
    next_ = f(now)
    total += next_
    now = next_
print(ans)


x = int(input())
print(x // 11 * 2 + (0 if x % 11 == 0 else (1 if x % 11 <= 6 else 2)))