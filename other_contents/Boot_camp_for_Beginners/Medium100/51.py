N = int(input())
X = list(map(int, input().split()))

X_sort = sorted(X)
X_left = X_sort[N//2 - 1]
X_right = X_sort[N//2 ]

for x in X:
    if x <= X_left:
        print(X_right)
    else:
        print(X_left)