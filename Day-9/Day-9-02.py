n=int(input())
s=0
temp=0
for i in range(1, n+1):
    a,b=map(int, input().split())
    s=s-a+b
    if s>temp:
        temp=s
print(temp)