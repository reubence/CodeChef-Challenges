for _ in range(int(input().strip())):
    n = int(input().strip())
    i = 5
    zeros =0
    while i<=n:
        zeros +=n//i
        i *=5
    print(zeros)