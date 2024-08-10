a=int(input())
rev_num=0
while a>0:
    digit=a%10
    rev_num=rev_num*10+digit
    a=a//10
print(rev_num)
