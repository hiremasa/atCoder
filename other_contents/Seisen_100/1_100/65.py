n,m,k=map(int,input().split())
edge=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    edge.append((c,a,b))
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
edge.sort()

def kruskal():
    uf = UnionFind(n)
    res = 0
    n_comp = n
    for i in range(m):
        c, a, b = edge[i]
        if n_comp == k:
            break
        if not (uf.same(a, b)):
            uf.union(a, b)
            res += c
            n_comp -= 1

    return res
print(kruskal())