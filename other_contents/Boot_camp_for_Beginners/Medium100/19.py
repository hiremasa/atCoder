R, G, B, N = map(int, input().split())
ans = 0
for r in range(N//R+1):
    for g in range(N//G+1):
        temp = (N - r * R - g * G)

        if 0 <=temp/B <=3000 and temp%B==0:
            ans += 1
print(ans)
