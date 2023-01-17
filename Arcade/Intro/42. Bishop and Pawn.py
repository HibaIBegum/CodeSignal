'''Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false.



'''


def solution(bishop, pawn):
    x = 'abcdefgh'
    bishop = x.index(bishop[0]), bishop[1]
    pawn = x.index(pawn[0]), pawn[1]
    if bishop[0] == pawn[0] or bishop[1] == pawn[1]:
        return False
    m = (int(bishop[1]) - int(pawn[1])) / (int(bishop[0]) - int(pawn[0]))
    if m == 1.0 or m == -1.0:
        return True
    return False


