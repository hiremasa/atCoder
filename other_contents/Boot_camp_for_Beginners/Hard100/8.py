N = int(input())

if __name__ =="__main__":
    if N & 1:
        ans = 0
    else:
        N //= 2
        ans = 0
        while N:
            N //= 5
            ans += N
    print(ans)
