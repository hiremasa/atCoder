# 孤立点

import numpy as np
import sys
buf = sys.stdin.buffer

H,W = map(int,buf.readline().split())
S = np.frombuffer(buf.read(H*(W+1)), dtype='S1').reshape((H,W+1))
S = S[:,:-1]

black = (S == b'#')
black_nbd = np.zeros((H,W), dtype=np.bool)

# 左
black_nbd[1:,:] |= black[:-1,:]
# 右
black_nbd[:-1,:] |= black[1:,:]
# 下
black_nbd[:,1:] |= black[:,:-1]
# 上
black_nbd[:,:-1] |= black[:,1:]

impossible = (black & ~black_nbd).any()
answer = 'Yes' if not impossible else 'No'
print(answer)