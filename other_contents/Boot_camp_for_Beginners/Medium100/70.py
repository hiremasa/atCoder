x, y = map(int, input().split())
cand = []
if x <= y:
    cand.append(y-x)
if (-x) <= y:
    cand.append(1 + x + y)
if x <= (-y):
    cand.append(1 - x - y)
if (-x) <= (-y):
    cand.append(2 - y + x)

answer = min(cand)
print(answer)
