class Uf:
	def __init__(self, N):
		self.p = list(range(N))
		self.rank = [0] * N
		self.size = [1] * N
	#検索 ノード番号を受け取って一番上の親ノードの番号を帰す
	def root(self, x):
		if self.p[x] != x:
			self.p[x] = self.root(self.p[x])

		return self.p[x]
	#同じ集合に属するか判定
	def same(self, x, y):
		return self.root(x) == self.root(y)
	#併合
	def unite(self, x, y):
		# 根を探す
		u = self.root(x)
		v = self.root(y)

		if u == v: return

		#木の高さを比較し、低いほうから高いほうに辺を張る
		if self.rank[u] < self.rank[v]:
			self.p[u] = v
			self.size[v] += self.size[u]
			self.size[u] = 0
		else:
			self.p[v] = u
			self.size[u] += self.size[v]
			self.size[v] = 0
			#木の高さが同じなら片方を1増やす
			if self.rank[u] == self.rank[v]:
				self.rank[u] += 1
	#ノード番号を受け取って、そのノードが含まれている集合のサイズを返す
	def count(self, x):
		return self.size[self.root(x)]

N, M, K = map(int, input().split())
uf=Uf(N)
res=[0]*N
for _ in range(M):
	a, b = map(int, input().split())
	a-=1
	b-=1
	res[a]-=1
	res[b]-=1
	uf.unite(a,b)

for _ in range(K):
	c, d =map(int, input().split())
	c-=1
	d-=1
	if uf.same(c,d):
		res[c]-=1
		res[d]-=1

for i in range(N):
	res[i]+=uf.count(i)-1
print(*res)
