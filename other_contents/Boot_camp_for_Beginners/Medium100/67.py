S = dict()
S['a'] = list(input())[::-1]
S['b'] = list(input())[::-1]
S['c'] = list(input())[::-1]

player = 'a'
while S[player]:
  player = S[player].pop()


answer = player.upper()
print(answer)

