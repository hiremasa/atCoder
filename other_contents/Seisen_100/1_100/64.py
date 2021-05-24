import heapq
V, E = map(int, input().split()) # 頂点、辺
adj = [ [] for v in range(V)] # 隣接リスト
for e in range(E):
    s, t, w = map(int, input().split())
    adj[s].append((t,w))
    adj[t].append((s,w))

visited = [0] * V # 訪問フラグ
pq = [] # 優先度付きキュー
for t, w in adj[0]: # 始点はどこでも良いので、0とする
    heapq.heappush(pq, (w, t))
visited[0] = 1 # 始点の訪問フラグを立てる

ans = 0
while(pq):
    w, t = heapq.heappop(pq)
    if visited[t]: # 訪問済みならスキップ
        continue
    visited[t] = 1 # 訪問フラグを立てる
    ans += w # スコアに加算
    for s, w in adj[t]: # 隣接する頂点を列挙
        if visited[s]==0: # 未訪問なら探索候補としてpqに追加
            heapq.heappush(pq, (w, s))
print (ans)