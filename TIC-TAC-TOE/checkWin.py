def checkWin():
    import main
    diag1 = (main.boardMatrix[0][0], main.boardMatrix[1][1], main.boardMatrix[2][2])
    diag2 = (main.boardMatrix[2][0], main.boardMatrix[1][1], main.boardMatrix[0][2])

    if all(x == 1 for x in (diag1)) or all(x == 2 for x in (diag1)):
        main.WIN_TYPE = 0
        return True
    
    if all(x == 1 for x in (diag2)) or all(x == 2 for x in (diag2)):
        main.WIN_TYPE = 1
        return True
    
    for z in range(0, 3):
        across = (main.boardMatrix[0][z], main.boardMatrix[1][z], main.boardMatrix[2][z])
        if all(x == 1 for x in (across)) or all(x == 2 for x in (across)):
            main.WIN_TYPE = 2
            main.WINNING = z
            return True
            
    for z in range(0, 3):
        down = (main.boardMatrix[z][0], main.boardMatrix[z][1], main.boardMatrix[z][2])
        if all(x == 1 for x in (down)) or all(x == 2 for x in (down)):
            main.WIN_TYPE = 3
            main.WINNING = z
            return True

    if main.VALID_CLICKS == 8:
        main.WIN_TYPE = 4
        return True

        
