for _ in range(int(input().strip())):
    for _ in range(int(input().strip())):
        I , N, Q = map(int,input().strip().split())
        if N%2 == 0:
            print(N//2)
        elif I==Q:
            print((N-1)//2)
        else:
            print((N//2)+1)