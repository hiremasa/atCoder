import numpy as np
W, H, N = map(int, input().split())
check_df = np.array(list([True] * W for _ in range(H)))

for _ in range(N):
    x, y, a = map(int, input().split())

    if a==1:
        check_df[:, :x] = False
    elif a==2:
        check_df[:, x:] = False
    elif a == 3:
        check_df[(H-y):, :] = False
    else:
        check_df[:(H-y), :] = False
    #print(check_df)
print(np.sum(check_df))