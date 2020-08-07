def fight(health,power):
    if power<=(health/2):
        print(0)
    else:
        while power>0:

            health = health-power
            if health>0:
                power = power/2
                if power<=0:
                    print(0)
                    break
            else:
                print(1)
                break


t=int(input().strip())
l=[]
for testcase in range(0,t):
    h,p = map(int,input().strip().split())
    a =[h,p]
    l.append(a)

for a in l:
    fight(int(a[0]),int(a[1]))
