'''Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.
https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
'''
def solution(cell1, cell2):
    col1 = ((ord(cell1[0])-ord('A')) + (ord(cell1[1])-ord('1'))) % 2 ==0
    col2 = ((ord(cell2[0])-ord('A')) + (ord(cell2[1])-ord('1'))) % 2 ==0
    print(col1,col2)
    print((ord(cell2[0])-ord('A')) + (ord(cell2[1])-ord('1'))%2)
    return col1 == col2


