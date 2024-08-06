#5/5 - test cases passed!
n,m = map(int, input().split())
c = list(map(int, input().split()))
items = []
res = []
for _ in range(m):
    p,w = map(int, input().split())
    items.append((p,w))
for k in c:
    max_wgt = 0
    for i,j in items:
        if i <= k:
            max_wgt += j
    res.append(max_wgt)
print(*res)
    
