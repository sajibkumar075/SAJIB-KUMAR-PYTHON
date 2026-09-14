s=input(" ")
sum=0
num=0
for i in s:
    if i.isupper():
        sum+=1
    else:
        num+=1
if sum>num:
     print(s.upper())
else:
     print(s.lower())