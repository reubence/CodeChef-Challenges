L = []
for _ in range(int(input().strip())):
    str = input().strip()
    mid = len(str)//2
    if len(str)%2==0:
        f = sorted(str[:mid])
        l = sorted(str[mid:])
    else:
        f = sorted(str[:mid])
        l = sorted(str[mid+1:])
    if l == f:
        L.append("YES")
    else:
        L.append("NO")
for i in L:
    print(i)