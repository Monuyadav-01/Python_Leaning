def fabo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fabo(n - 1) + fabo(n - 2)


print(fabo(10))
