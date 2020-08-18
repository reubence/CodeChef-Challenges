from collections import Counter
N = []
K = []
Fam = []
for _ in range(int(input())):
    n , k = map(int,input().split())
    N.append(n)
    K.append(k)
    Fam.append(list(map(int,input().split())))

for num,F in enumerate(Fam):
    T = []
    T_temp = []
    T2 = []
    j = 0
    arguments = 0
    args = False
    for i in range(len(F)):
        try:
            if F[i]==F[i+1]:
                T_temp.append(F[j:i+1])
                j = i+1
        except IndexError:
            T_temp.append(F[j:i+1])
    for i in range(len(F)):
        try:
            if F[i]==F[i+1] or F[i+1] in F[j:i+1]:
                T2.append(F[j:i+1])
                args = True
                temp = F[j:i+2]
                c = Counter(temp)
                temp_arguments = 0
                for elem in (set(temp)):
                    if c[elem]>1:
                        temp_arguments+=c[elem]
                if temp_arguments<=K[num]:  #and len(set(F[i+2:]))==len(F[i+2:]) and F[i+2] not in F[j:i+1]:
                    continue
                # elif len(set(F[i+2:]))<=len(F[i+2:]) and len(F[i+2:])!=1:
                else:
                    T.append(F[j:i+1])
                    j = 1+i
                    continue
                # else:
                #     continue
            else:
                continue
        except IndexError:
            T2.append(F[j:i + 1])
            T.append(F[j:i+1])
    # print(T)
    if args==True:
        for table in T:
            cn = Counter(table)
            for elem in set(cn):
                if cn[elem] >1:
                    arguments+=cn[elem]
        fam_args = 0
        cns = Counter(Fam[0])
        for elem in set(cns):
            if cns[elem]>1:
                fam_args +=cns[elem]
        print(min(K[num] * len(T) + arguments,K[num] * len(T2) + arguments,K[num]+fam_args,K[num]*len(T_temp)))
        print(len(T_temp))
    else:
        print(K[num] * len(T))


