N = int(input())
S = map(int, input().split())
Q = int(input())
T = map(int, input().split())

set_S = set(S)
set_T = set(T)
ans = len(set_S & set_T)
print(ans)


def is_ok():
    return S[i] <= t
