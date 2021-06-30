import heapq
V, E, r = map(int, input().split())

G = [[] for _ in range(V)]

for _ in range(E):
    s, t, w = map(int, input().split())
    G[s].append([w, t])
    G[t].append([w, s])


#init
pq = []
Distance = [float("inf")] * V
heapq.heappush(pq, [0, r])
Distance[r] = 0

while pq:
    w, node = heapq.heappop(pq)
    Distance[node] = w
    if Distance[node] < w:
        continue
    for next_w, next_node in G[node]:
        if Distance[next_node] > Distance[node] + next_w:
            heapq.heappush(pq, [Distance[node] + next_w, next_node])
print(*Distance)




# coding=utf-8

N, M = map(int, input().split())

class UnionFind:
    def __init__(self, number_of_objects):
        self.groups_dic = {}
        self.groups_list = []
        self.number_of_objects = number_of_objects
        self.parent_pointers = list(range(self.number_of_objects))

    def find(self, x):
        if self.parent_pointers[x] == x:
            return x
        else:
            return self.find(self.parent_pointers[x])

    def unit(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        else:
            self.parent_pointers[max(x, y)] = min(x, y)
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def groups(self):
        """ グループとその集合をリストで返す """
        for k in range(self.number_of_objects):
            self.parent_pointers[k] = self.find(self.parent_pointers[k])
        for j in range(self.number_of_objects):
            if self.parent_pointers[j] not in self.groups_dic:
                self.groups_dic[self.parent_pointers[j]] = [j]
            else:
                self.groups_dic[self.parent_pointers[j]].append(j)
        for group in self.groups_dic.values():
            self.groups_list.append(group)
        return list(self.groups_list)

uf = UnionFind(N+1)  # atcoderは1~ 最後に-1する
non_tree = []
for _ in range(M):
    u, v = map(int, input().split())
    if uf.same(u, v):
        non_tree.append(u)
    uf.unit(u, v)

# print(non_tree)
# print(uf.parent_pointers)
uf.groups()
for i in range(len(non_tree)):
    non_tree[i] = uf.parent_pointers[non_tree[i]]

print(len(set(uf.parent_pointers))-len(set(non_tree))-1)
