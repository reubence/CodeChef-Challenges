for _ in range(int(input().strip())):
    s = input().strip()
    c = list(map(int,input().strip().split()))
    q = int(input().strip())
    for i in range(q):
        c2 = list(map(int,input().strip().split()))
        s = [c2[0]-c[0],c2[1]-c[1]]
        count = 0
        x = []
        y = []
        if s[0]>0 and s[1]>0:
            for j in range(s[0]):
