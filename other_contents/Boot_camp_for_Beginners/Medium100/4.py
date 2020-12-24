S = str(input())
N = len(S)
for i in range(N-1, 0, -1):
	par_S = S[:i]
	len_pS = len(par_S)

	if par_S[(len_pS//2):] == par_S[0:(len_pS//2)]:
		print(len_pS)
		exit()