def merge(hight):
    if len(hight) == 0:
        return 0
    if len(hight) == 1:
        return hight[0]
    m = min(hight)
    m_idx = hight.index(m)
    hight = [h - m for h in hight]
    left_hight = hight[:m_idx]
    right_hight = hight[m_idx + 1:]
    return  merge(left_hight) + merge(right_hight) + m

if __name__ == '__main__':
    N = int(input())
    h = list(map(int, input().split()))
    print(merge(h))