N = int(input())

now_x, now_y = 0, 0
now_t = 0
for i in range(N):
    t, x, y = map(int, input().split())

    dis = abs(now_x - x) + abs(now_y - y)
    del_t = t - now_t

    if (dis - del_t) % 2 == 0 and del_t >= dis:
        now_x, now_y = x, y
        now_t = t

    else:
        exit(print("No"))
print("Yes")
