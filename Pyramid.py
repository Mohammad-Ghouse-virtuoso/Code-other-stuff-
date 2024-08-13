n = int(input())
num = 2
res = n * 1
for i in range(0, n, n-1):
  res += 2 * i * num
  num += 1 
print(res)
