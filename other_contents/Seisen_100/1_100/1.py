while(True):
    N, X = map(int, input().split())
    if N == 0:
        break

    ans = 0
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            for k in range(j + 1, N + 1):
                if i + j + k == X:
                    ans += 1

    print(ans)