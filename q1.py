s1=input()
s2=input()
c=1
for i in s1:
    if(i in s2):
        c=1
    else:
        c=0
if c==1:
    print("string balanced")
else:
    print("not balanced")
    
