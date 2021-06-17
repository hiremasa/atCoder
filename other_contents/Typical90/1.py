N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split())) #len == N + 1

def is_ok(d):
    last = 0
    cnt_cut = 0
    for i in range(N):
        if A[i] - last >= d and L - A[i] >= d:
            cnt_cut += 1
            last = A[i]
        if cnt_cut == K:
            return True
    return False


def meguru_bisect(ng, ok):
    while abs(ng-ok)>1:
        mid=(ng+ok)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

print(meguru_bisect(10**9+1, 0))