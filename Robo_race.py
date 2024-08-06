x,m,y,n=map(int,input().split()) time=max(x,y) 
while True:
  if time>=x and (time-x)%m==0 and  time>=y and (time-y)%n==0:
    print(time)
    break
  time += 1
