S = sorted(input())
T = sorted(input(), reverse=True)

S = "".join(S)
T = "".join(T)

if S<T:
    exit(print("Yes"))
else:
    exit(print("No"))