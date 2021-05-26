import heapq
while True:

    n = int(input())
    if n == 0:
        exit()
    XYZ = []
    for _ in range(n):
        x, y, z, r = map(float, input().split())
        XYZ.append([x, y, z, r])
    D = [[float("inf")] * n for _ in range(n)]
    for i in range(n - 1):
        xi, yi, zi, ri = XYZ[i]
        for j in range(i + 1, n):
            xj, yj, zj, rj = XYZ[j]

            d = ((xi - xj)**2 + (yi - yj)**2 + (zi - zj)** 2)**(1/2)
            if d <= ri + rj:
                D[i][j] = 0
                D[j][i] = 0
            else:
                D[i][j] = d - (ri + rj)
                D[j][i] = d - (ri + rj)

    visited = [0] * n
    pq = []
    for i, d in enumerate(D[0]):
        heapq.heappush(pq, (d, i))
    visited[0] = 1
    ans = 0
    while pq:
        cost_i, i = heapq.heappop(pq)
        if visited[i] == 1:
            continue
        visited[i] = 1
        ans += cost_i

        for j, cost_j in enumerate(D[i]):
            if visited[j] == 0:
                heapq.heappush(pq, (cost_j, j))
    print("{:.3f}".format(round(ans,3)))


