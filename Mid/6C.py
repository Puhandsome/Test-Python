a = None
b = None
n = input()
maxDiff = 0
while n != "$":
  n = int(n)
  if not a:
    a = n
  else:
    a,b = int(n),a
    diff = abs(a-b)
    if maxDiff < diff:
        maxDiff = diff
  n = input()
if a and b:
  print(maxDiff)
else:
  print("Insufficient data")