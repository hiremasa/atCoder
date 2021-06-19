import itertools
N = int(input())
ans = []

if N % 2 == 0:
    for i in itertools.product([0, 1], repeat = N):
        if i.count(1) == N//2:
            zero_count = 0
            flag = True
            word = ""
            for j in range(N):
                if i[j] == 0:
                    zero_count += 1
                elif i[j] == 1:
                    if zero_count >= 1:
                        zero_count -= 1
                    else:
                        flag = False
                word += str(i[j])
            if flag:
                ans.append(word.replace("0", "(").replace("1", ")"))

ans.sort()
print(*ans ,sep = "\n")

# def check(S):
#     cnt = 0

#     for s in S:
#         if sn== "(":
#             cnt += 1
#         elif s == ")":
#             cnt -= 1

#         if cnt < 0:
#             return False

#     if cnt == 0:
#         return True
#     else:
#         return False

# if __name__ == "__main___":

    # if N % 2 == 1:
    #     exit(print())

    # S_list = list(itertools.product(["(", ")"], repeat=N-2))

    # for S in S_list:
    #     if check(S):
    #         print(*S)

