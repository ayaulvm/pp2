l = int(input("First: "))
r = int(input("Second: "))

def squares(l, r):
    for i in range(l, r + 1):
        yield i ** 2

print(*squares(l, r), sep=', ')