N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]

dp[0][A[0]] = 1
for i in range(1, N - 1):
    a = A[i]
    for j in range(21):
        if j - a >= 0:
            dp[i][j] += dp[i - 1][j - a]
        if j + a <= 20:
            dp[i][j] += dp[i - 1][j + a]
print(*dp)
print(dp[N - 2][A[N - 1]])

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
import heapq
import math
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement, permutations
from bisect import bisect_left


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [[0] * (21) for i in range(n)]
    dp[0][nums[0]] = 1
    for i in range(1, n - 1):
        for j in range(21):
            if j - nums[i] >= 0:
                dp[i][j] += dp[i - 1][j - nums[i]]
            if j + nums[i] < 21:
                dp[i][j] += dp[i - 1][j + nums[i]]
    
    print(dp[n - 2][nums[n - 1]])
    return
        

if __name__ == "__main__":
    main()
"""