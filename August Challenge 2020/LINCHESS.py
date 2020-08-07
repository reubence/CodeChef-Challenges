n = int(input().strip())
square = []
for i in range(n):
    numPlayer , chef = map(int,input().strip().split())
    playerPawn = list(filter(lambda x: x <= chef,list(map(int,input().strip().split()))))

    moves = []
    og_steps = []
    for k in range(len(playerPawn)):
        if chef % playerPawn[k]  == 0:
            moves.append((chef//playerPawn[k])-1)
            og_steps.append(playerPawn[k])
            # print(moves)
            # print(og_steps)
        else:
            continue
    # for index, value in enumerate(moves):
    #     # print("yo")
    #     if value == min(moves):
    #         print(og_steps[index])
    #         break
    # else:
    #     print("-1")
    if moves:
        x = min(moves)
        y = moves.index(x)
        print(og_steps[y])
    else:
        print(-1)

