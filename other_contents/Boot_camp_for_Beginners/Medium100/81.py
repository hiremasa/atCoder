S = input()

import itertools

print(len(list(itertools.groupby(S))) - 1)