from fractions import gcd
A, B, C, D = map(int, input().split())
def solve(N):
    ans = N
    ans -= N//C
    ans -= N//D
    ans += N//(C*D//gcd(C, D))
    return ans
print(solve(B) - solve(A-1))