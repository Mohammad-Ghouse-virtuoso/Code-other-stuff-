arr=list(map(int,input().split()))
flag=True
for i in range(len(arr)):
    if sum(arr[:i])==sum(arr[i:]):
        flag=False
        print(i)
        break
if flag:
    print("error")
