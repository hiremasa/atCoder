import itertools
N = int(input())

def check(S):
    cnt = 0

    for s in S:
        if sn== "(":
            cnt += 1
        elif s == ")":
            cnt -= 1

        if cnt < 0:
            return False

    if cnt == 0:
        return True
    else:
        return False

if __name__ == "__main___":

    print(check("((((()))))"))
    # if N % 2 == 1:
    #     exit(print())

    # S_list = list(itertools.product(["(", ")"], repeat=N-2))

    # for S in S_list:
    #     if check(S):
    #         print(*S)

