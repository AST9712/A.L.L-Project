<<<<<<< HEAD
def checkWin():
    import main    
    diag1 = (main.board.boardMatrix[0][0], main.board.boardMatrix[1][1], main.board.boardMatrix[2][2])
    diag2 = (main.board.boardMatrix[2][0], main.board.boardMatrix[1][1], main.board.boardMatrix[0][2])
    
    for z in range(0, 3):
        across = (main.board.boardMatrix[0][z], main.board.boardMatrix[1][z], main.board.boardMatrix[2][z])
        if all(x == 1 for x in (across)) or all(x == 2 for x in (across)):
            return True
            
    for z in range(0, 3):
        down = (main.board.boardMatrix[z][0], main.board.boardMatrix[z][1], main.board.boardMatrix[z][2])
        if all(x == 1 for x in (down)) or all(x == 2 for x in (down)):
            return True

    if all(x == 1 for x in (diag1)) or all(x == 2 for x in (diag1)):
        return True
    
    if all(x == 1 for x in (diag2)) or all(x == 2 for x in (diag2)):
        return True

=======
#0 is draw, 1 is X, 2 is O

test = [[0 for x in range(3)] for y in range(3)]

for x in range(3):
    test[0][x] = 23
    test[1][x] = 5
    test[2][x] = 66



def checkWin():
    print(all(x == test[0][0] for x in test))

        
checkWin()
>>>>>>> 0faff18b5846ce74fb382bb8ff0f607edbe47a63
