def countdown(n):
    if n==0:
        return "Done"
    print(n)
    return countdown(n-1)
print(countdown(10))
