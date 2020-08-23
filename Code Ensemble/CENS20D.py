for _ in range(int(input().strip())):
    n = int(input().strip())
    num = list(map(int,input().strip().split()))
    count = 0
    pairs = []
    if n > 1:
        for x,valm in enumerate(num):
            for y,valy in enumerate(num):
                if x<y:
                    bitwiseis = num[x] & num[y]
                    if bitwiseis == num[x]:
                        pairs.append([x,y])
        print(len(pairs))
    else:
        print(0)