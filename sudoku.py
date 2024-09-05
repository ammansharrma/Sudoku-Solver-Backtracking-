import pyautogui as pg
import numpy as np
import time

grid = []

while True:
    row = list((input('Row :')))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid)==9:
        break
    print('Row '+str(len(grid)) + ' Completed')
    print()

#time.sleep(1)



grid = [[1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9]]
#------  Code for checking element n in grid is possible or not ------------
def possible(x,y,n):
    #For checking rows
    for i in range(0,9):
        if(grid[i][x]==n and i!=y):
            return False
    #for checking columns
    for i in range(0,9):
        if grid[y][i]==n and i!=x :
            return False
        
    # for checking individual boxes
    x0 = (x//3)*3
    y0 =(y//3)*3
    for X in range(x0,x0+3):
        for Y in range(y0,y0+3):
            if grid[X][Y]==n:
                return False
    return True

#Printing the Matrix
def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])
    
    for lists in final:
        for num in lists:
            str_fin.append(str(num))
    
    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey("right")
        counter.append(num)
        if(len(counter)%9==0):
            pg.hotkey("down")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
        



# Bracktracking Function
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    input('more?')

solve()
Print(grid)