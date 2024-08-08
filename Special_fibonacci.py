num = int(input())
f = [1,1]
for i in range(2, num+1):
  val = f[n-1]*f[n-1]+f[n-2]*f[n-2]
  val = val % 47
  f.append(val)
print(f[-1])
