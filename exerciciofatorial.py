def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n*fatorial(n-1)

fatorial(4)