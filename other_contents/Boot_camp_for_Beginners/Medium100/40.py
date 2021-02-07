import numpy as np
N, M = map(int, input().split())
X = np.sort(np.array(input().split(), dtype=np.int32))

if N >= M:
    exit(print(0))

X_diff = np.sort(np.diff(X))
remove = X_diff[-N+1:]
ans = X[-1] - X[0] - np.sum(remove)
print(ans)
