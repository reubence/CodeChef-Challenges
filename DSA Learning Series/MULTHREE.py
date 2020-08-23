for _ in range(int(input().strip())):
    sum = 0
    temp = 0
    k, n, m = map(int,input().split())
    sum = n+m
    temp = (n+m)%10
    if k ==2:
        if sum%3==0:
            print("YES")
            break
        else:
            print("NO")
            break
    else:
        sum+=temp
        noOfGroups = (k-3)//4
        remainingDigits = (k-3)%4
        sum+=noOfGroups*20
        for i in range(remainingDigits):
            if i ==0:
                sum+=(2*temp)%10
            elif i==1:
                sum+=(4*temp)%10
            elif i==2:
                sum+=(8*temp)%10

        if sum%3 ==0:
            print("YES")
        else:
            print("NO")

