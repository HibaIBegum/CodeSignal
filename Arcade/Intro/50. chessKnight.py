'''Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.
For cell = "a1", the output should be
solution(cell) = 2.'''
def solution(cell):
    cnt =0
    row = ord(cell[1]) - ord('0')
    col = ord(cell[0]) - ord('a')+ 1
    steps = [
        [-2,-1], [-1,-2], [-2,1], [-1,2], [2,-1], [1,-2], [2,1], [1,2]
        ]
    for i in range(len(steps)):
        tmprow = row + steps[i][0]
        tmpcol = col + steps[i][1]
        if (tmprow>=1 and tmprow<=8) and (tmpcol>=1 and tmpcol<=8):
            cnt +=1
    return cnt


