H,W = map(int,input().split())

A = [input() for _ in range(H)]

bl = True
x,y = 0,0
for _ in range(H+W-2):
  if x+1 < H and A[x+1][y] == '#':
    x += 1
    continue
  if y+1 < W and A[x][y+1] == '#':
    y += 1
    continue
  bl = False
  break

bl = bl and (sum(x.count('#') for x in A) == H+W-1)
answer = 'Possible' if bl else 'Impossible'
print(answer)
