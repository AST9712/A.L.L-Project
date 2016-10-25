def checkValidClick(coords):
    import main
    x, y = coords
    
    if x < 200 and y < 200:       
        if main.board.boardMatrix[0][0] == 0:
            #drawX(40, -10)
            main.drawO(18, -70)
            main.board.boardMatrix[0][0] = 1        
        
    elif x < 400 and y < 200:
        if main.board.boardMatrix[1][0] == 0: 
            main.drawX(240, -10)
            main.board.boardMatrix[1][0] = 1
        
    elif x < 600 and y < 200:
        if main.board.boardMatrix[2][0] == 0: 
            main.drawX(440, -10)
            main.board.boardMatrix[2][0] = 1

    elif x < 200 and y < 400:
        if main.board.boardMatrix[0][1] == 0: 
            main.drawX(40, 190)
            main.board.boardMatrix[0][1] = 1

    elif x < 400 and y < 400:
        if main.board.boardMatrix[1][1] == 0: 
            main.drawX(240, 190)
            main.board.boardMatrix[1][1] = 1

    elif x < 600 and y < 400:
        if main.board.boardMatrix[2][1] == 0: 
            main.drawX(440, 190)
            main.board.boardMatrix[2][1] = 1

    elif x < 200 and y < 600:
        if main.board.boardMatrix[0][2] == 0: 
            main.drawX(40, 390)
            main.board.boardMatrix[0][2] = 1

    elif x < 400 and y < 600:
        if main.board.boardMatrix[1][2] == 0: 
            main.drawX(240, 390)
            main.board.boardMatrix[1][2] = 1

    elif x < 600 and y < 600:
        if main.board.boardMatrix[2][2] == 0: 
            main.drawX(440, 390)
            main.board.boardMatrix[2][2] = 1

