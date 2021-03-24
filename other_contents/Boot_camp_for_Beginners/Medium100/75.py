#=====================-自作 何故か通らない
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
Te = ["r", "s", "p"]


def janken(t, te):
    if t == "r":
        if te == "p":
            return P
        else:
            return 0
    elif t == "s":
        if te == "r":
            return R
        else:
            return 0
    else:
        if te == "s":
            return S
        else:
            return 0

#groupごとに最大化
def max_group(k):
    par_T = T[k:-1:K]

    total = 0

    for first_te in Te : #最初の手を選ぶ

        temp = janken(par_T[0], first_te)
        prev_te = first_te
        for i in range(1, len(par_T)):
            Ti = par_T[i]
            Te_ = [te for te in Te if te != prev_te]

            result_0 = janken(Ti, Te_[0])
            result_1 = janken(Ti, Te_[1])
            if result_0 > result_1:
                te = Te_[0]
                temp += result_0
                prev_te = te
            else:
                te = Te_[1]
                temp += result_1
                prev_te = te

        total = max(total, temp)
    return total

ans = 0
for k in range(K):
    print(T[k:N+1:K])
    ans += max_group(k)
print(ans)


#=========================AC
"""
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())


ans = 0
commands = [''] * N
for i, t in enumerate(T):
    if t == 'r':
        command = 'p'
        point = P

    elif t == 's':
        command = 'r'
        point = R

    elif t == 'p':
        command = 's'
        point = S

    if (i - K >= 0) and (commands[i -  K] == command):
        command = ''
        point = 0

    ans += point
    commands[i] = command

print(ans)
"""