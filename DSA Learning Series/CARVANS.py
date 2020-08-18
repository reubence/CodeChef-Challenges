for _ in range(int(input())):
    input()
    s = list(map(int, input().split()))
    c, cms = 0, 2 ** 32
    for i in s:
        if i <= cms:
            c += 1
            cms = i
    print(c)