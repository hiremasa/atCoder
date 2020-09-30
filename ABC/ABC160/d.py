import heapq
from collections import defaultdict, Counter
N, X, Y = map(int, input().split())
#隣接行列
D=defaultdict(lambda: defaultdict(lambda: float("inf")))
for i in range(N-1):
	D[i][i]=0
	D[i][i+1]=1
	D[i+1][i]=1
D[X-1][Y-1]=1
D[Y-1][X-1]=1

"""
#TLEする
def warshall_floyd(d, V): 
	for k in range(V):
		for i in range(V):
			for j in range(V):
				d[i][j] = min(d[i][j], d[i][k] + d[k][j])

	return d #d[i][j]に頂点i, j間の最短距離を格納

d=warshall_floyd(D, N)

ans=[0]*N
for k in range(1, N):
	for i in range(N-1):
		for j in range(i+1,N):
			ans[d[i][j]]+=1
print(*[i//(N-1) for i in ans[1:]], sep="\n")
"""


class Dijkstra:
	# 計算量 O((E+V)logV)
 
	# adjは2次元defaultdict
	def dijkstra(self, adj, start, goal=None):
 
		self.dist = defaultdict(lambda: float("inf"))  # 始点から各頂点までの最短距離を格納する
		self.prev = defaultdict(lambda: float("inf"))  # 最短経路における，その頂点の前の頂点のIDを格納する
 
		#num = len(adj)  # グラフのノード数
		#dist = [float('inf') for i in range(num)]
		#prev = [float('inf') for i in range(num)]
 
		self.dist[start] = 0
		q = []  # プライオリティキュー．各要素は，(startからある頂点vまでの仮の距離, 頂点vのID)からなるタプル
		heapq.heappush(q, (0, start))  # 始点をpush
 
		while len(q) != 0:
			prov_cost, src = heapq.heappop(q)  # pop
 
			# プライオリティキューに格納されている最短距離が，現在計算できている最短距離より大きければ，distの更新をする必要はない
			if self.dist[src] < prov_cost:
				continue
 
			# 探索で辺を見つける場合ここに書く
 
			# 他の頂点の探索
			for dest, cost in adj[src].items():
				if self.dist[dest] > self.dist[src] + cost:
					self.dist[dest] = self.dist[src] + cost  # distの更新
					heapq.heappush(q, (self.dist[dest], dest))  # キューに新たな仮の距離の情報をpush
					self.prev[dest] = src  # 前の頂点を記録
 
		if goal is not None:
			return self.get_path(goal, self.prev)
		else:
			return self.dist
 
	def get_path(self, goal, prev):
		path = [goal]  # 最短経路
		dest = goal
 
		# 終点から最短経路を逆順に辿る
		while prev[dest] != float('inf'):
			path.append(prev[dest])
			dest = prev[dest]
 
		# 経路をreverseして出力
		return list(reversed(path))


d=Dijkstra()
ans=[0]*N
for i in range(N):
	dd=d.dijkstra(D, i)
	for j in range(N):
		ans[dd[j]]+=1
print(*[i//2 for i in ans[1:]], sep="\n")
#print(Counter((d.dijkstra(D, 1))))
#print(d.dijkstra(D, 2))

