s = input()
q = int(input())
turn = 0
# ともにSに近い方から並べる
before = "" 
after = ""
for _ in range(q):
    tmp = input()
    if tmp=="1":
        turn += 1
    else:
        _,f,c = tmp.split()
        f = int(f)
        if (turn + f) % 2 == 1:
            before += c
        else:
            after += c
if turn%2==0:
    out = before[::-1] + s + after
else:
    out = after[::-1] + s[::-1] + before
print(out)
