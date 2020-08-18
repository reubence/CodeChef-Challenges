num = []
for _ in range(int(input().strip())):
    num.append(input().strip())
for i in num:
    print(int(i[::-1]))