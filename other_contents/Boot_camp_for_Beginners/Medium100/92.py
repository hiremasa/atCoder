a, b, x = map(int, input().split())

half = a ** 2 * b / 2

if x <= half:
    #a ** 2 * a * np.tan(theta) / 2 = x
    theta = np.arctan(2 * x /a**2/a)
    print(np.rad2deg(theta))
else:


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from math import atan,tan,pi

a,b,x = map(int,read().split())

def max_volume(theta):
    # 弧度法にする
    theta = theta/180*pi
    if theta<atan(b/a):
        # 半分より上のパターン
        area = a*b-a*a*tan(theta)/2
    else:
        area = b*(b/tan(theta))/2
    return area*a

left = 0 # おさまっている
right = 90 # あふれている
while right - left > 1e-7:
    mid = (left+right)/2
    if max_volume(mid) <= x:
        right = mid
    else:
        left = mid

answer = (left+right)/2
print(answer)