class Solution:
    def intToRoman(self, num: int) -> str:
        di={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans=0
        for i in range(len(num)):
            if(i+1<len(num) and di[num[i]]<di[num[i+1]]):
                ans=di[num[i]]
            else:
                ans+=di[num[i]]
        return ans
---------------------Def method above-------------------------------------
num=int(input())
n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]
s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X","IX","V", "IV", "I"]
res=""
for i in range(len(n)):
    while num>=n[i]:
        res=res+s[i]
        num-=n[i]
print(res)
