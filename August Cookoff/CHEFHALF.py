for _ in range(int(input().strip())):
    n = int(input().strip())
    seq = list(map(int,input().strip().split()))
    counter = 0
    for i in range(0,(n/2)-1,3):
        while len(seq)%2!=0:
            fh = seq[:(len(seq) / 2) + 1]
            sh = seq[(len(seq) / 2) + 1:]
            if max(fh)<min(sh) or min(fh)>max(sh):
                counter+=1
            for k in range(2,len(fh),2):
                for j in range(0,len(seq),k):
                    fh = seq[j:j+2]
                    sh = seq[j+2:]
        newseq = seq[i+1:]
        newseq.append(seq[:i+1])
        seq.append(newseq)


