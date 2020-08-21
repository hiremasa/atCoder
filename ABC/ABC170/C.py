X, N =map(int, input().split())
p_list=list(map(int, input().split()))
#i=N
#1st Xがp_listにあるか
	#あれば+=!
	#なければ答え
#|X-i|=1がp_listにあるか
	#あれば+=!
	#なければ答え

i=N
j=0
while True:
	if X-j not in p_list:
		print(X-j)
		exit()
	elif X+j not in p_list:
		print(X+j)
		exit()
	else:
		j+=1

