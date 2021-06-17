N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def is_ok(d):
    last = 0
    for i in range(1, K):
        crt = last + 1
        while crt < N and A[crt] - A[last] < d:
            crt += 1
        if crt == N:
            return False
        last = crt
    return True

def meguru_bisect(ng, ok):
    while abs(ng-ok)>1:
        mid=(ng+ok)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

print(meguru_bisect(100000+1, 0))