a,y = map(int, input().split())
res = 0
while True:
if a%y==0:
  res=y
  break
else:
  y+=1
s=0
while res>0:
  n=res%10
  s+=n
  res=res//10
print(s)
