N = int(input())
A = list(map(int, input().split()))
four, one, two = 0, 0, 0
for a in A:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two = 1
    else:
        one += 1



if four + 1 >= one + two:
    print("Yes")
else:
    print("No")

