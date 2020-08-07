n = int(input().strip())
import math
roof = []
for i in range(n):
    powers = list(map(int,input().strip().split()))
    roof.append([math.ceil(x/9) for x in powers])
for i in roof:
    if i[0]==i[1]:
        print("1",i[1])
    else:
        if i[0]>i[1]:
            print("1",i[1])
        else:
            print("0",i[0])
