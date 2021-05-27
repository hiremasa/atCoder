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

#Kruskal
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

while 1:
    n = int(input())
    if n == 0:
        break
    xyzr = [list(map(float, input().split())) for _ in range(n)]
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = xyzr[i][0] - xyzr[j][0]
            dy = xyzr[i][1] - xyzr[j][1]
            dz = xyzr[i][2] - xyzr[j][2]
            d = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
            edges.append([i, j, max(0, d - xyzr[i][3] - xyzr[j][3])])
            
    edges.sort(key = lambda x:x[2])
    ans = 0
    UF = UnionFind(n)
    for i, j, w in edges:
        if not UF.same(i, j):
            UF.union(i, j)
            ans += w
    print("{:.3f}".format(ans))
    
    
