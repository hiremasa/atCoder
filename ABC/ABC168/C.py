A, B, H, M = map(int,input().split())

import numpy as np
theta_h=2*np.pi*(H/12 + M/720)#rad
theta_m=2*np.pi*M/60#rad
theta=min((max(theta_h, theta_m)-min(theta_h, theta_m)), 2*np.pi-(max(theta_h, theta_m)-min(theta_h, theta_m)))
print(np.sqrt(A**2 + B**2 - 2*np.cos(theta)*A*B))