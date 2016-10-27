#0 is draw, 1 is X, 2 is O

test = [[0 for x in range(3)] for y in range(3)]

for x in range(3):
    test[0][x] = 23
    test[1][x] = 5
    test[2][x] = 66



def checkWin():
    print(all(x == test[0][0] for x in test))

        
checkWin()
