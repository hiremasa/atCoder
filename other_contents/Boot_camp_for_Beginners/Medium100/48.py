W, H, x, y = map(int, input().split())

S = W * H /2

if (W == 2*x and H == 2*y):
    print(S, 1)
else:
    print(S, 0)