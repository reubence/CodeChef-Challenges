for _ in range(int(input().strip())):
    n,k = map(int,input().strip().split())
    w = list(map(int,input().strip().split()))
    carry = 0
    trips = 0
    if max(w)>k:
        print("-1")
    else:
        i = 0
        while w[i]:
            carry+=w[i]
            if carry>k:
                trips+=1
                carry = 0
            elif i == len(w)-1:
                trips+=1
                break
            else:
                i+=1
        print(trips)
