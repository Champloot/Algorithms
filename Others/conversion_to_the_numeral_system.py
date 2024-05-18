def func(a, s):
  num = ""
  while a != 0:
    num = f"{a%s}" + num
  return num

# number in the decimal system
a = int(input())
# decimal system
s = int(input())
print(func(a,s))
