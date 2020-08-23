from sys import stdin, stdout
n , m = map(int,stdin.readline().strip().split())
mat = []
for x in range(n):
    mat.append(list(map(int,stdin.readline().strip())))
q = int(stdin.readline().strip())
coords = []
for x in range(q):
    coords.append(list(map(int,stdin.readline().split())))
for l in coords:
    for i in range(l[0]-1,l[2]):
        for j in range(l[1]-1,l[3]):
            mat[i][j] = 1 - mat[i][j]
for a in mat:
    for b in a:
        stdout.write(str(b))
    stdout.write('\n')


