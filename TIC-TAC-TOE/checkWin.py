def checkWin():
    import main    
    diag1 = (main.board.boardMatrix[0][0], main.board.boardMatrix[1][1], main.board.boardMatrix[2][2])
    diag2 = (main.board.boardMatrix[2][0], main.board.boardMatrix[1][1], main.board.boardMatrix[0][2])
    
    for z in range(0, 3):
        across = (main.board.boardMatrix[0][z], main.board.boardMatrix[1][z], main.board.boardMatrix[2][z])
        if all(x == 1 for x in (across)) or all(x == 2 for x in (across)):
            main.WINNING_HORIZ = z
            return True
            
    for z in range(0, 3):
        down = (main.board.boardMatrix[z][0], main.board.boardMatrix[z][1], main.board.boardMatrix[z][2])
        if all(x == 1 for x in (down)) or all(x == 2 for x in (down)):
            return True

    if all(x == 1 for x in (diag1)) or all(x == 2 for x in (diag1)):
        return True
    
    if all(x == 1 for x in (diag2)) or all(x == 2 for x in (diag2)):
        return True


        
