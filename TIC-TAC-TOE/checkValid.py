def checkValidClick(coords):
    import main
    x, y = coords
    
    if x < 200 and y < 200:       
        if main.board.boardMatrix[0][0] == 0:
            if main.PLYR_X == True:
                main.drawX(40, -10)
            else:
                main.drawO(18, -70)
            main.board.boardMatrix[0][0] = 1
            main.PLYR_X = not main.PLYR_X
        
    elif x < 400 and y < 200:
        if main.board.boardMatrix[1][0] == 0:
            if main.PLYR_X == True:
                main.drawX(240, -10)
            else:
                main.drawO(218, -70)            
            main.board.boardMatrix[1][0] = 1
            main.PLYR_X = not main.PLYR_X
        
    elif x < 600 and y < 200:
        if main.board.boardMatrix[2][0] == 0: 
            if main.PLYR_X == True:
                main.drawX(440, -10)
            else:
                main.drawO(418, -70)   
            main.board.boardMatrix[2][0] = 1
            main.PLYR_X = not main.PLYR_X

    elif x < 200 and y < 400:
        if main.board.boardMatrix[0][1] == 0:
            if main.PLYR_X == True:
                main.drawX(40, 190)
            else:
                main.drawO(18, 130) 
            #main.drawX(40, 190)
            main.board.boardMatrix[0][1] = 1
            main.PLYR_X = not main.PLYR_X

    elif x < 400 and y < 400:
        if main.board.boardMatrix[1][1] == 0:
            if main.PLYR_X == True:
                main.drawX(240, 190)
            else:
                main.drawO(218, 130) 
            #main.drawX(240, 190)
            main.board.boardMatrix[1][1] = 1
            main.PLYR_X = not main.PLYR_X

    elif x < 600 and y < 400:
        if main.board.boardMatrix[2][1] == 0:
            if main.PLYR_X == True:
                main.drawX(440, 190)
            else:
                main.drawO(418, 130) 
            #main.drawX(440, 190)
            main.board.boardMatrix[2][1] = 1
            main.PLYR_X = not main.PLYR_X

    elif x < 200 and y < 600:
        if main.board.boardMatrix[0][2] == 0:
            if main.PLYR_X == True:
                main.drawX(40, 390)
            else:
                main.drawO(18, 330) 
            #main.drawX(40, 390)
            main.board.boardMatrix[0][2] = 1
            main.PLYR_X = not main.PLYR_X

    elif x < 400 and y < 600:
        if main.board.boardMatrix[1][2] == 0:
            if main.PLYR_X == True:
                main.drawX(240, 390)
            else:
                main.drawO(218, 330) 
            #main.drawX(240, 390)
            main.board.boardMatrix[1][2] = 1
            main.PLYR_X = not main.PLYR_X

    elif x < 600 and y < 600:
        if main.board.boardMatrix[2][2] == 0:
            if main.PLYR_X == True:
                main.drawX(440, 390)
            else:
                main.drawO(418, 330) 
            #main.drawX(440, 390)
            main.board.boardMatrix[2][2] = 1
            main.PLYR_X = not main.PLYR_X
