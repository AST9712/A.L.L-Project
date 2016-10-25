def checkValidClick():
    
    x, y = pygame.mouse.get_pos()
    
    if x < 200 and y < 200:       
        if board.boardMatrix[0][0] == 0:
            #drawX(40, -10)
            drawO(18, -70)
            board.boardMatrix[0][0] = 1        
        
    elif x < 400 and y < 200:
        if board.boardMatrix[1][0] == 0: 
            drawX(240, -10)
            board.boardMatrix[1][0] = 1
        
    elif x < 600 and y < 200:
        if board.boardMatrix[2][0] == 0: 
            drawX(440, -10)
            board.boardMatrix[2][0] = 1

    elif x < 200 and y < 400:
        if board.boardMatrix[0][1] == 0: 
            drawX(40, 190)
            board.boardMatrix[0][1] = 1

    elif x < 400 and y < 400:
        if board.boardMatrix[1][1] == 0: 
            drawX(240, 190)
            board.boardMatrix[1][1] = 1

    elif x < 600 and y < 400:
        if board.boardMatrix[2][1] == 0: 
            drawX(440, 190)
            board.boardMatrix[2][1] = 1

    elif x < 200 and y < 600:
        if board.boardMatrix[0][2] == 0: 
            drawX(40, 390)
            board.boardMatrix[0][2] = 1

    elif x < 400 and y < 600:
        if board.boardMatrix[1][2] == 0: 
            drawX(240, 390)
            board.boardMatrix[1][2] = 1

    elif x < 600 and y < 600:
        if board.boardMatrix[2][2] == 0: 
            drawX(440, 390)
            board.boardMatrix[2][2] = 1        
    

