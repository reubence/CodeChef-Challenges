for _ in range(int(input().strip())):
    n = int(input().strip())
    v = []
    for i in range(n):
        v.append(list(map(int,input().strip().split())))
    nsides = n
    a = n//2
    while a>=3:
        nsides+=a
        a=a//2
    print(nsides)