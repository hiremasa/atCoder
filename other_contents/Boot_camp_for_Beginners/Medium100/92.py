a, b, x = map(int, input().split())

half = a ** 2 * b / 2

if x <= half:
    #a ** 2 * a * np.tan(theta) / 2 = x
    theta = np.arctan(2 * x /a**2/a)
    print(np.rad2deg(theta))
else:

import math
a,b,x = map(int,input().split())
if x >= a*a*b/2:
  ans = math.degrees(math.atan(2*b/a-2*x/a**3))
else:
  ans = math.degrees(math.atan(a*b**2/(2*x)))
print(ans)