N, M = map(int, input().split())
print(int((100*(N - M) + 1900 * M) / .5 ** M))