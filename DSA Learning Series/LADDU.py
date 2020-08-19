for _ in range(int(input())):
    a, o = input().split()
    r = 400
    if o[0] == "I": r = 200
    l = 0
    for i in range(int(a)):
        x = input()
        if x[0] == "T":
            l += 300
        elif x[0] == "B":
            l += int(x.split()[1])
        elif x[8] == "H":
            l += 50
        else:
            rnk = int(x.split()[1])
            l += 300 + (20 - rnk if rnk < 21 else 0)
    print(l // r)
