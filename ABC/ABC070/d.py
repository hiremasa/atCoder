import heapq
from collections import defaultdict, Counter
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

N=int(input())
D=defaultdict(lambda: defaultdict(lambda: float("inf")))
for i in range(N-1):
	a, b , c = map(int, input().split())
	a-=1
	b-=1
	D[a][b]=c
	D[b][a]=c
for i in range(N): D[i][i]=0


dij=Dijkstra()
Q, K = map(int, input().split())
K-=1
dd=dij.dijkstra(D, K)
for _ in range(Q):
	x, y = map(int, input().split())
	x-=1
	y-=1
	print(dd[x]+dd[y])



