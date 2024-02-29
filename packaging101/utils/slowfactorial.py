def slowfactorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * slowfactorial(n-1)
