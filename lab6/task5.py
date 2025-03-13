#Write a Python program with builtin function that returns True if all elements of the tuple are true.

def all_true(t):
    return all(t)  


t1 = tuple(map(int, input().split()))

print(all_true(t1))


