from graphics import *
from squares import *
import time

def drawGrid(window):
    grid = []
    
    all_cords = [[50, 400, 100, 350], [100, 400, 150, 350], [150, 400, 200, 350],
                 [200, 400, 250, 350], [250, 400, 300, 350], [300, 400, 350, 350],
                 [350, 400, 400, 350], [400, 400, 450, 350],[50, 350, 100, 300],
                 [100, 350, 150, 300], [150, 350, 200, 300], [200, 350, 250, 300],
                 [250, 350, 300, 300], [300, 350, 350, 300], [350, 350, 400, 300],
                 [400, 350, 450, 300],[50, 300, 100, 250], [100, 300, 150, 250],
                 [150, 300, 200, 250], [200, 300, 250, 250], [250, 300, 300, 250],
                 [300, 300, 350, 250], [350, 300, 400, 250],[400, 300, 450, 250],
                 [50, 250, 100, 200], [100, 250, 150, 200], [150, 250, 200, 200],
                 [200, 250, 250, 200], [250, 250, 300, 200], [300, 250, 350, 200],
                 [350, 250, 400, 200], [400, 250, 450, 200], [50, 200, 100, 150],
                 [100, 200, 150, 150], [150, 200, 200, 150], [200, 200, 250, 150],
                 [250, 200, 300, 150], [300, 200, 350, 150], [350, 200, 400, 150],
                 [400, 200, 450, 150], [50, 150, 100, 100], [100, 150, 150, 100],
                 [150, 150, 200, 100], [200, 150, 250, 100], [250, 150, 300, 100],
                 [300, 150, 350, 100], [350, 150, 400, 100],[400, 150, 450, 100],
                 [50, 100, 100, 50], [100, 100, 150, 50], [150, 100, 200, 50],
                 [200, 100, 250, 50], [250, 100, 300, 50], [300, 100, 350, 50],
                 [350, 100, 400, 50], [400, 100, 450, 50]]      



    grid = [[0]*7 for i in range(8)]
    x =0
    y = 0
    
    for cd in all_cords:
                sq = make_square(cd[0],cd[1],cd[2],cd[3])
                grid[x][y] = sq
                shape = Rectangle(grid[x][y].a, grid[x][y].b)
                
                if (x + y) % 2 == 0:
                    shape.setFill('orange')
                else:
                    shape.setFill('yellow')
                    
                shape.draw(window)
                x +=1
                if x == 8:                    
                    x = 0
                    y+=1

    return grid
def drawCross(square,box):

    line1 = Line(square.cross1, square.cross2)
    line1.setWidth(8)
    line2 = Line(square.cross3, square.cross4)
    line2.setWidth(8)
    line1.draw(box)
    line2.draw(box)    
    return

def drawCircle(square ,box):

    circle = Circle(square.mid, square.circleRadius)
    circle.setWidth(8)
    circle.draw(box)
    
    return

def checkAllConditions(matrix, x_pos, y_pos, checker):

    condition = ''

    if (0 <= y_pos <= 3) and (3 <= x_pos <= 7) and (condition == ''):
        back_diagnal_check = ((matrix[x_pos-1][y_pos+1].checker == checker) and
                        (matrix[x_pos-2][y_pos+2].checker == checker) and
                        (matrix[x_pos-3][y_pos+3].checker == checker))
        if back_diagnal_check == True:
            condition = 'bd'
        
    if (0 <= y_pos <= 3) and (0 <= x_pos <= 4) and (condition == ''):
        forward_diagnal_check = ((matrix[x_pos+1][y_pos+1].checker == checker) and
                        (matrix[x_pos+2][y_pos+2].checker == checker) and
                        (matrix[x_pos+3][y_pos+3].checker == checker))
        if forward_diagnal_check == True:
            condition = 'fd'
    if (0 <= x_pos <= 4) and (condition == ''):
        horizontal_check = ((matrix[x_pos+1][y_pos].checker == checker) and
                        (matrix[x_pos+2][y_pos].checker == checker) and
                        (matrix[x_pos+3][y_pos].checker == checker))
        if horizontal_check == True:
            condition = 'h'
    if (0 <= y_pos <= 3) and (condition == ''):
        vertical_check = ((matrix[x_pos][y_pos+1].checker == checker) and
                        (matrix[x_pos][y_pos+2].checker == checker) and
                        (matrix[x_pos][y_pos+3].checker == checker))
        if vertical_check == True:
            condition = 'v'

    
    return condition


def DrawWinningLine(p1,p2,box):
    point1, point2 = p1,p2
    line = Line(point1,point2)
    line.setWidth(7)
    line.setFill('red')
    line.draw(box)

def CreateButton(box):
    time.sleep(1)
    p1 = Point(105, 345)
    p2 = Point(395, 245)
    window = Rectangle(p1, p2)
    window.setFill('grey')
    window.draw(box)
    
    gameover = 'Game Over. Play again?'
    label = Text(Point(250, 320), gameover)
    label.setSize(10)
    label.draw(box)

    pt1 = Point(210,260)
    pt2 = Point(250, 290)
    yes_button = Rectangle(pt1, pt2)
    yes_button.setFill('green')
    yes_button.draw(box)
    
    label = Text(Point(229, 275), 'Yes')
    label.setSize(9)
    label.draw(box)
    
    
    while True:
        mouse = box.getMouse()
        if (250 > mouse.x > 210) and (290 > mouse.y > 260):
            box.close()
            Main()
        
    
    
    

def checkConnection(square, matrix, box):


    win = 0
    for col in matrix:
        for sqr in col:
            
            pstn_x = matrix.index(col)
            pstn_y = col.index(sqr)
            winning_condition = checkAllConditions(matrix, pstn_x, pstn_y, sqr.checker)
            
            if (sqr.checker == square.checker) and (winning_condition == 'v'):
                point1, point2 = matrix[pstn_x][pstn_y].mid, matrix[pstn_x][pstn_y+3].mid
                DrawWinningLine(point1,point2,box)
                win = sqr.checker
                
            elif (sqr.checker == square.checker) and (winning_condition == 'h'):
                point1, point2 = matrix[pstn_x][pstn_y].mid, matrix[pstn_x+3][pstn_y].mid
                DrawWinningLine(point1,point2,box)
                win = sqr.checker
                                                                    
            elif (sqr.checker == square.checker) and (winning_condition == 'fd'):
                point1, point2 = matrix[pstn_x][pstn_y].mid, matrix[pstn_x+3][pstn_y+3].mid
                DrawWinningLine(point1,point2,box)
                win = sqr.checker
                
            elif (sqr.checker == square.checker) and (winning_condition == 'bd'):
                point1, point2 = matrix[pstn_x][pstn_y].mid, matrix[pstn_x-3][pstn_y+3].mid
                DrawWinningLine(point1,point2,box)
                win = sqr.checker

    return win


def displayNoOfMoves(moves, box):
    global moves_label
    moves_label.undraw()
    message = 'Moves: ' + str(moves)
    moves_label.setText(message)
    moves_label.setSize(10)
    moves_label.draw(box)

def displayNextPlayer(player, box):
    global player_label
    player_label.undraw()
    message = "Next move: Player " +  str(player)
    player_label.setText(message)
    player_label.setSize(10)
    player_label.draw(box)

moves_label = Text(Point(400, 450), '')
player_label =  Text(Point(130, 450), '')


def play(box, matrix):

    player = 1
    moves = 0
    winner = 0
    displayNoOfMoves(moves, box)
    displayNextPlayer(player, box)    
    while True:        
        mouse = box.getMouse()
        
        
        for col in matrix:
            for sqr in col:                 
                if (sqr.x2 > mouse.x > sqr.x1) and (sqr.y1 > mouse.y > sqr.y2):
                    if player == 1 and sqr.checker == 0:
                        drawCircle(sqr, box)
                        sqr.checker = 1
                        if checkConnection(sqr, matrix, box) == 1:
                            winner = 1
                        player = 2
                        moves +=1
                        
                    elif player == 2 and sqr.checker == 0:
                        drawCross(sqr,box)
                        sqr.checker = 2
                        if checkConnection(sqr, matrix, box) == 2:
                            winner = 2
                        player = 1
                        moves +=1
        displayNoOfMoves(moves, box)
        displayNextPlayer(player, box)
                        
        if (winner >= 1) or (moves == 56):
            winning_label = Text(Point(250, 470), '')
            if (winner>=1):
                if player == 2:
                    player = 1
                elif player == 1:
                    player =2
                message = 'Player '+ str(player) + ' has won.'
                winning_label.setText(message)
            elif(moves == 56) and (winner ==0):
                winning_label.setText('Tie game')
            winning_label.setSize(10)
            winning_label.draw(box)
            CreateButton(box) ## waits for 1 second before appearing. Also asks to play new game.
            break
      
## winner displayed above grid.       

    return




def game():
    win = GraphWin('Tic-Tac-Toe',500,600)
    yMax = 500
    xMax = 500
    win.setCoords(0,0,xMax,yMax)
    
    grid = drawGrid(win)
    play(win, grid)
    
    time.sleep(10)
    win.close()
          
def Main():
    game()
if __name__ == '__main__':
    Main()
