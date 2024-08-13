def solve(n, salt, pepper): 
  s,p=0,0
  r=[]
  for i in range(len(salt)): 
    r.append(salt[i] pepper[i]) 
  return max(r)

n=int(input()) 
salt=list(map(int,input().split()))  
pepper=list(map(int,input().split())) 
res=solve(n, salt,pepper)
print(res)
