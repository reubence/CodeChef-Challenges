t=int(input())
l=[]
co=[]
for i in range(t):
    n=int(input())
    l.append(n)
l=list(sorted(l))
for i in range(t):
    co.append(l[i]*(t-i))
print(max(co))