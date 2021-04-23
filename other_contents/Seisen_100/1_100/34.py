n = int(input())

#再帰　遅い
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def Fib(n):
    a, b = 1, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n - 1):
            a, b = b, a + b
        return b

print(Fib(n))