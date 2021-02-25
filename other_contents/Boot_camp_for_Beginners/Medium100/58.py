N,A,B,C,D = map(int,input().split())
S = input()

def test(x,y):
  # xからyへ行ける
  substr = S[x:y-1]
  return substr.find('##') == -1

bl = test(A,C) and test(B,D)
if C > D:
  # 追い越す必要がある
  # 道の存在は保証されているので、局所的に詰まないようにBを配置できればよい
  can_swap = False
  for b in range(B-1,D):
    if S[b] == '#':
      continue
    if S[b-1] == '.' and S[b+1] == '.':
      can_swap = True
      break
  bl = bl and can_swap
answer = 'Yes' if bl else 'No'
print(answer)
