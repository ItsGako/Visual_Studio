def recursivite(n):
    if n==0:
        return 1
    else:
        return n / recursivite(n-1)

print(recursivite(3))