import math
while True:
    sdomain = []
    squares = input()

    for s in squares:
        if s == '0':
            sdomain.append(['1','2','3','4','5','6','7','8','9'])
        elif s == ' ':
            continue
        else:
            sdomain.append([s])

    if len(sdomain) != 81:
        print("not 81 numbers")
        quit()
    flag = 0
    cnt = 0
    broken = 0
    iguess = 0
    while True:  
        solved = 0
        for i in range(0, len(sdomain)):
            if len(sdomain[i]) == 0:
                broken = 1
                break
            if len(sdomain[i]) != 1:
                for e in range(0,9):
                    r = math.floor(i/9) * 9
                    if len(sdomain[r+e]) == 1 and r+e != i:
                        if sdomain[r+e][0] in sdomain[i]:
                            sdomain[i].remove(sdomain[r+e][0])
                    c = (i%9) + 9*e
                    if len(sdomain[c]) == 1 and c != i:
                        if sdomain[c][0] in sdomain[i]:
                            sdomain[i].remove(sdomain[c][0])
                    reg = (math.floor(i/9) * 9 + math.floor((i%9)/3) * 3) % 9 + 27*math.floor(i/27)
                    if e < 3:
                        if len(sdomain[reg+e]) == 1 and reg+e != i:
                            if sdomain[reg+e][0] in sdomain[i]:
                                sdomain[i].remove(sdomain[reg+e][0])
                    elif e < 6:
                        if len(sdomain[reg + 9 + e%3]) == 1 and reg + 9 + e%3 != i:
                            if sdomain[reg+ 9 + e%3][0] in sdomain[i]:
                                sdomain[i].remove(sdomain[reg + 9 + e%3][0])
                    else:
                        if len(sdomain[reg + 18 + e%3]) == 1 and reg + 18 + e%3 != i:
                            if sdomain[reg+ 18 + e%3][0] in sdomain[i]:
                                sdomain[i].remove(sdomain[reg + 18 + e%3][0])
            else:
                solved = solved + 1
        if solved == 81:
            flag = 1

        if broken == 1:
            sdomain = []
            for g in guess:
                if len(g) > 1:
                    sdomain.append(g.copy())
                else:
                    sdomain.append(g)
            sdomain[iguess] = sdomain[iguess][1]
            broken = 0
        

        for n in ['1','2','3','4','5','6','7','8','9']:
            for c in range(0, 9):
                count = 0
                index = 0
                for e in range(0, 9):
                    if n in sdomain[e + c*9]:
                        count = count + 1
                        index = (e + c*9)
                if count == 1:
                    sdomain[index] = n

            for c in range(0, 9):
                count = 0 
                index = 0
                for e in range(0,9):
                    if n in sdomain[c + e*9]:
                        count = count + 1
                        index = c + e*9 
                if count == 1:
                    sdomain[index] = n

            
            for c in range(0,9):
                count = 0
                index = 0
                for e in range(0,9):
                    i = (c%3)* 3+ (27*math.floor(c/3)) + e%3 + (9*math.floor(e/3))
                    if n in sdomain[i]:
                        count = count + 1
                        index = i
                if count == 1:
                    sdomain[index] = n

        if flag == 1:
            print("\n")
            print(sdomain[0], " ", sdomain[1], " ", sdomain[2], "   ", sdomain[3], " ", sdomain[4], " ", sdomain[5], "   ", sdomain[6], " ", sdomain[7], " ", sdomain[8])
            print(sdomain[9], " ", sdomain[10], " ", sdomain[11], "   ", sdomain[12], " ", sdomain[13], " ", sdomain[14], "   ", sdomain[15], " ", sdomain[16], " ", sdomain[17])
            print(sdomain[18], " ", sdomain[19], " ", sdomain[20], "   ", sdomain[21], " ", sdomain[22], " ", sdomain[23], "   ", sdomain[24], " ", sdomain[25], " ", sdomain[26])
            print("\n")
            print(sdomain[27], " ", sdomain[28], " ", sdomain[29], "   ", sdomain[30], " ", sdomain[31], " ", sdomain[32], "   ", sdomain[33], " ", sdomain[34], " ", sdomain[35])
            print(sdomain[36], " ", sdomain[37]," ", sdomain[38], "   ", sdomain[39], " ", sdomain[40], " ", sdomain[41], "   ", sdomain[42], " ", sdomain[43], " ", sdomain[44])
            print(sdomain[45], " ", sdomain[46], " ", sdomain[47], "   ", sdomain[48], " ", sdomain[49], " ", sdomain[50], "   ", sdomain[51], " ", sdomain[52], " ", sdomain[53])
            print("\n")
            print(sdomain[54], " ", sdomain[55], " ", sdomain[56], "   ", sdomain[57], " ", sdomain[58], " ", sdomain[59], "   ", sdomain[60], " ", sdomain[61], " ", sdomain[62])
            print(sdomain[63], " ", sdomain[64], " ", sdomain[65], "   ", sdomain[66], " ", sdomain[67], " ", sdomain[68], "   ", sdomain[69], " ", sdomain[70], " ", sdomain[71])
            print(sdomain[72], " ", sdomain[73], " ", sdomain[74], "   ", sdomain[75], " ", sdomain[76], " ", sdomain[77], "   ", sdomain[78], " ", sdomain[79], " ", sdomain[80])
            print("\n")
            exit()

        if cnt == 50:
            guess = []
            cnt = 0
            for s in sdomain:
                if len(s) > 1:
                    guess.append(s.copy())
                else:
                    guess.append(s)

            for i in range(0, len(sdomain)):
                if len(sdomain[i]) == 2:
                    sdomain[i] = sdomain[i][0]
                    iguess = i
                    break
        else:
            cnt = cnt + 1
                