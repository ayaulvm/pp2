a = 33
b = 200

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")