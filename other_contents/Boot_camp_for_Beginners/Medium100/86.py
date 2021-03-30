N = int(input())
a_list = list(map(int, input().split()))

a_set = set(a_list)

if len(a_set) == 1:
    if sum(a_set) == 0:
        print("Yes")
    else:
        print("No")

elif len(a_set) == 2:
    a_1, _2 = sorted(a_set)
    if a_1 == 0:
        if a_list.count(a_1) * 3 == N:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

elif len(a_set) == 3:
    a_1, a_2, a_3 = a_set
    if a_list.count(a_1) == a_list.count(a_2) and a_list.count(a_2) == a_list.count(a_3):
        if a_1 ^ a_2 == a_3:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
"""
from collections import Counter
s = set(A)
c = Counter(A)
if all(A) == 0:
    print("Yes")
elif len(s) == 2:
    if 0 in s:
        _, x = sorted(s)
        if c[0] * 3 == N and c[x] == 2 * N //3:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
elif len(s) == 3:
    x, y, z = sorted(s)
    if c[x] == c[y] == c[z]:
        if x ^ y == z:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
"""