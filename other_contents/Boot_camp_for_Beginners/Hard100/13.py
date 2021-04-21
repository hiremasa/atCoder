N = int(input())
S = input()
ans = 0
for T in range(1000):
    if T < 10:
        temp = "00" + str(T)
    elif T < 100:
        temp = "0" + str(T)
    else:
        temp = str(T)

    t_i = 0
    for j in range(len(S)):
        if temp[t_i] == S[j]:
            t_i += 1
        if t_i == 3:
            ans += 1
            break
print(ans)
