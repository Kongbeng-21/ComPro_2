def rec(n):
    if n == 0:
        return 0
    return rec(n-1) + 1

print(rec(5))
